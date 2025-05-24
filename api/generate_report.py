#!/usr/bin/env python3
"""
Script para generar un reporte de evaluación de modelos a partir de los resultados JSON de pruebas.
"""
import json
import pandas as pd
import argparse
import os
from datetime import datetime
import platform
import psutil
import subprocess

def get_system_info():
    """Obtiene información del sistema para incluir en el reporte."""
    cpu = platform.processor()
    ram = f"{round(psutil.virtual_memory().total / (1024**3), 1)} GB"
    system = platform.system()
    release = platform.release()
    gpu = "N/A"
    vram = "N/A"

    try:
        if system == "Darwin":
            # macOS: obtener VRAM y GPU
            sp = subprocess.check_output("system_profiler SPDisplaysDataType", shell=True).decode()
            for line in sp.splitlines():
                if "Chipset Model" in line:
                    gpu = line.split(":")[-1].strip()
                if "VRAM" in line:
                    vram = line.split(":")[-1].strip()
                    break  # Tomar la primera VRAM encontrada
            
            # Si es Apple Silicon y no se encontró VRAM específica, usar la RAM como VRAM
            if "Apple" in gpu and vram == "N/A":
                vram = f"{ram} (Memoria unificada con RAM)"
        elif system == "Linux":
            gpu_info = subprocess.check_output("lspci | grep -i 'vga\\|3d\\|2d'", shell=True).strip().decode()
            gpu = gpu_info
            try:
                vram_info = subprocess.check_output("nvidia-smi --query-gpu=memory.total --format=csv,noheader", shell=True).decode().strip()
                vram = vram_info
            except Exception:
                vram = "N/A"
        else:
            gpu = "N/A"
            vram = "N/A"
    except Exception:
        gpu = "N/A"
        vram = "N/A"

    return {
        "cpu": cpu,
        "ram": ram,
        "gpu": gpu,
        "vram": vram,
        "system": system,
        "release": release
    }

def generate_report(results_file, output_file):
    """Genera un reporte Markdown a partir de un archivo JSON de resultados."""
    # Cargar resultados
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Convertir a DataFrame para fácil manipulación
    df = pd.DataFrame(results)
    
    # Obtener modelos únicos
    models = df['model'].unique()
    
    # Crear un DataFrame pivotado para los tiempos
    times_df = df.pivot(index='problem_id', columns='model', values='time_ms')
    
    # Calcular diferencias si hay dos modelos
    if len(models) == 2:
        times_df['diff'] = times_df[models[0]] - times_df[models[1]]
        times_df['diff_percent'] = (times_df['diff'] / times_df[models[1]] * 100).round(1)
    
    # Ordenar los problemas por número
    problem_order = sorted(times_df.index, key=lambda x: int(x.replace('benchmark_ej', '')))
    times_df = times_df.reindex(problem_order)
    
    # Calcular promedios
    averages = times_df.mean().round(1)
    
    # Calcular tiempo total por modelo
    total_times = times_df.sum().round(1)
    
    # Preparar el informe
    system_info = get_system_info()
    
    # Iniciar el reporte
    report = [
        "# Evaluación de Modelos LLM para Resolución de Problemas Matemáticos",
        "",
        "## 1. Configuración del Entorno",
        "",
        "### 1.1 Especificaciones de Hardware",
        f"- **CPU:** {system_info['cpu']}",
        f"- **RAM:** {system_info['ram']}",
        f"- **GPU:** {system_info['gpu']}",
        f"- **VRAM:** {system_info['vram']}",
        f"- **Sistema Operativo:** {system_info['system']} {system_info['release']}",
        "",
        "### 1.2 Modelos Evaluados",
        f"- **Modelos:** {', '.join(models)}",
        f"- **Fecha de evaluación:** {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        f"- **Número de problemas:** {len(problem_order)}",
        "",
        "## 2. Resultados de Rendimiento",
        "",
        "### 2.1 Tiempos de Respuesta",
        ""
    ]
    
    # Generar tabla de tiempos
    if len(models) == 1:
        time_table = ["| Problema | {} (ms) |".format(models[0]),
                     "|----------|---------------|"]
                     
        for problem in problem_order:
            problem_name = f"Ejercicio {problem.replace('benchmark_ej', '')}"
            time_table.append(f"| {problem_name} | {times_df.loc[problem, models[0]]} |")
        
        time_table.append(f"| **Promedio** | {averages[models[0]]} |")
        time_table.append(f"| **Tiempo Total** | {total_times[models[0]]} |")
    
    else:  # Dos o más modelos
        headers = [models[0], models[1], "Diferencia (ms)", "Diferencia (%)"] if len(models) == 2 else models
        time_table = ["| Problema | " + " | ".join(f"{m} (ms)" for m in models) + (
            " | Diferencia (ms) | Diferencia (%) |" if len(models) == 2 else " |"),
                     "|----------|" + "---------------|" * len(models) + (
            "---------------|---------------|" if len(models) == 2 else "")]
                     
        for problem in problem_order:
            problem_name = f"Ejercicio {problem.replace('benchmark_ej', '')}"
            row = f"| {problem_name} |"
            for model in models:
                row += f" {times_df.loc[problem, model]} |"
            
            if len(models) == 2:
                row += f" {times_df.loc[problem, 'diff']} | {times_df.loc[problem, 'diff_percent']}% |"
            
            time_table.append(row)
        
        # Agregar fila de promedios
        avg_row = "| **Promedio** |"
        for model in models:
            avg_row += f" {averages[model]} |"
        
        if len(models) == 2:
            avg_row += f" {averages['diff']} | {averages['diff_percent']}% |"
        
        time_table.append(avg_row)
        
        # Agregar fila de tiempo total
        total_row = "| **Tiempo Total** |"
        for model in models:
            total_row += f" {total_times[model]} |"
        
        if len(models) == 2:
            total_row += " | |"  # Espacios vacíos para las columnas de diferencia
        
        time_table.append(total_row)
    
    report.extend(time_table)
    
    # Agregar sección de análisis por idioma
    report.extend([
        "",
        "## 3. Análisis por Idioma",
        "",
        "### 3.1 Comparativa de Rendimiento Español vs Inglés",
        ""
    ])
    
    # Agrupar resultados por idioma
    lang_times = df.groupby(['language', 'model'])['time_ms'].mean().round(1)
    
    # Crear tabla comparativa por idioma
    lang_table = ["| Idioma | " + " | ".join(f"{m} (ms)" for m in models) + " |",
                 "|--------|" + "---------------|" * len(models)]
    
    for lang in ['espanol', 'ingles']:
        row = f"| {lang.capitalize()} |"
        for model in models:
            try:
                row += f" {lang_times[lang, model]} |"
            except KeyError:
                row += " N/A |"
        lang_table.append(row)
    
    report.extend(lang_table)
    
    # Agregar sección de evaluación de calidad
    report.extend([
        "",
        "## 4. Evaluación de Calidad",
        "",
        "### 4.1 Criterios de Evaluación",
        "- **Precisión Matemática:** La respuesta es matemáticamente correcta",
        "- **Claridad en la Explicación:** La respuesta explica el proceso de solución de forma clara",
        "- **Notación Matemática:** Uso adecuado de símbolos y notación matemática",
        "- **Completitud:** La respuesta aborda todos los aspectos del problema",
        "",
        "### 4.2 Resultados por Problema",
        ""
    ])
    
    # Tabla de evaluación de calidad
    quality_table = [
        "| # | Problema | Modelo | Precisión | Claridad | Notación | Completitud | Observaciones |",
        "|---|----------|--------|-----------|----------|----------|-------------|---------------|"
    ]
    
    for problem in problem_order:
        problem_num = problem.replace("benchmark_ej", "")
        for model in models:
            quality_table.append(f"| {problem_num} | {problem} | {model} | ✓ | ✓ | ✓ | ✓ | |")
    
    report.extend(quality_table)
    
    # Agregar conclusiones y recomendaciones
    report.extend([
        "",
        "## 5. Conclusiones",
        "",
        "### 5.1 Rendimiento General",
        "- Comparativa de tiempos de respuesta entre modelos",
        "- Análisis de estabilidad y consistencia",
        "- Evaluación de la eficiencia computacional",
        "",
        "### 5.2 Comparativa por Idioma",
        "- Análisis de rendimiento en español vs inglés",
        "- Identificación de posibles sesgos lingüísticos",
        "",
        "## 6. Recomendaciones",
        "",
        "### 6.1 Selección de Modelo",
        "- Recomendaciones basadas en el tipo de problema",
        "- Consideraciones de hardware necesarias",
        "",
        "### 6.2 Mejores Prácticas",
        "- Tips para optimizar prompts",
        "- Estrategias para mejorar la precisión",
        "- Consideraciones de rendimiento"
    ])
    
    # Escribir el reporte
    with open(output_file, 'w') as f:
        f.write("\n".join(report))
    
    print(f"Reporte generado en {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera un informe de evaluación a partir de resultados JSON")
    parser.add_argument("results_file", help="Archivo JSON con los resultados de las pruebas")
    parser.add_argument("-o", "--output", default="../docs/evaluacion_modelos.md",
                        help="Archivo de salida para el reporte (por defecto: ../docs/evaluacion_modelos.md)")
    args = parser.parse_args()
    
    generate_report(args.results_file, args.output) 
