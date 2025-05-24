# Evaluación de Modelos LLM para Resolución de Problemas Matemáticos

## 1. Configuración del Entorno

### 1.1 Especificaciones de Hardware
- **CPU:** arm
- **RAM:** 16.0 GB
- **GPU:** Apple M2 Pro
- **VRAM:** 16.0 GB (Memoria unificada con RAM)
- **Sistema Operativo:** Darwin 24.4.0

### 1.2 Modelos Evaluados
- **Modelos:** llama2, llama3.2
- **Fecha de evaluación:** 24/05/2025 18:19
- **Número de problemas:** 30

## 2. Resultados de Rendimiento

### 2.1 Tiempos de Respuesta

| Problema | llama2 (ms) | llama3.2 (ms) | Diferencia (ms) | Diferencia (%) |
|----------|---------------|---------------|---------------|---------------|
| Ejercicio 1 | 8122 | 4798 | 3324 | 69.3% |
| Ejercicio 2 | 13891 | 10233 | 3658 | 35.7% |
| Ejercicio 3 | 20094 | 8436 | 11658 | 138.2% |
| Ejercicio 4 | 12503 | 6138 | 6365 | 103.7% |
| Ejercicio 5 | 7197 | 16059 | -8862 | -55.2% |
| Ejercicio 6 | 5586 | 6144 | -558 | -9.1% |
| Ejercicio 7 | 7930 | 3179 | 4751 | 149.4% |
| Ejercicio 8 | 3943 | 2331 | 1612 | 69.2% |
| Ejercicio 9 | 3664 | 4796 | -1132 | -23.6% |
| Ejercicio 10 | 22130 | 9599 | 12531 | 130.5% |
| Ejercicio 11 | 6884 | 6618 | 266 | 4.0% |
| Ejercicio 12 | 8900 | 5385 | 3515 | 65.3% |
| Ejercicio 13 | 9891 | 2143 | 7748 | 361.5% |
| Ejercicio 14 | 5778 | 4310 | 1468 | 34.1% |
| Ejercicio 15 | 11299 | 7047 | 4252 | 60.3% |
| Ejercicio 16 | 3349 | 3204 | 145 | 4.5% |
| Ejercicio 17 | 13242 | 5171 | 8071 | 156.1% |
| Ejercicio 18 | 16832 | 5870 | 10962 | 186.7% |
| Ejercicio 19 | 10855 | 5255 | 5600 | 106.6% |
| Ejercicio 20 | 14080 | 8043 | 6037 | 75.1% |
| Ejercicio 21 | 5282 | 3446 | 1836 | 53.3% |
| Ejercicio 22 | 8134 | 2753 | 5381 | 195.5% |
| Ejercicio 23 | 5500 | 7697 | -2197 | -28.5% |
| Ejercicio 24 | 5538 | 3262 | 2276 | 69.8% |
| Ejercicio 25 | 4394 | 10058 | -5664 | -56.3% |
| Ejercicio 26 | 5907 | 2924 | 2983 | 102.0% |
| Ejercicio 27 | 7931 | 20432 | -12501 | -61.2% |
| Ejercicio 28 | 12038 | 5021 | 7017 | 139.8% |
| Ejercicio 29 | 8427 | 3320 | 5107 | 153.8% |
| Ejercicio 30 | 6685 | 3979 | 2706 | 68.0% |
| **Promedio** | 9200.2 | 6255.0 | 2945.2 | 76.6% |
| **Tiempo Total** | 276006.0 | 187651.0 | | |

## 3. Análisis por Idioma

### 3.1 Comparativa de Rendimiento Español vs Inglés

| Idioma | llama2 (ms) | llama3.2 (ms) |
|--------|---------------|---------------|
| Espanol | 9854.1 | 6481.1 |
| Ingles | 8546.3 | 6029.0 |

## 4. Evaluación de Calidad

### 4.1 Criterios de Evaluación
- **Precisión Matemática:** La respuesta es matemáticamente correcta
- **Claridad en la Explicación:** La respuesta explica el proceso de solución de forma clara
- **Notación Matemática:** Uso adecuado de símbolos y notación matemática
- **Completitud:** La respuesta aborda todos los aspectos del problema

### 4.2 Resultados por Problema

| # | Problema | Modelo | Precisión | Claridad | Notación | Completitud | Observaciones |
|---|----------|--------|-----------|----------|----------|-------------|---------------|
| 1 | benchmark_ej1 | llama2 | ✓ | ✓ | ✓ |  | |
| 1 | benchmark_ej1 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 2 | benchmark_ej2 | llama2 | ✓ | ✓ | ✓ |  | |
| 2 | benchmark_ej2 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 3 | benchmark_ej3 | llama2 | ✓ | ✓ |  | ✓ | |
| 3 | benchmark_ej3 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 4 | benchmark_ej4 | llama2 | ✓ | ✓ | ✓ |  | |
| 4 | benchmark_ej4 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 5 | benchmark_ej5 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 5 | benchmark_ej5 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 6 | benchmark_ej6 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 6 | benchmark_ej6 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 7 | benchmark_ej7 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 7 | benchmark_ej7 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 8 | benchmark_ej8 | llama2 | ✓ |  | ✓ | ✓ | |
| 8 | benchmark_ej8 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 9 | benchmark_ej9 | llama2 | ✓ | ✓ | ✓ |  | |
| 9 | benchmark_ej9 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 10 | benchmark_ej10 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 10 | benchmark_ej10 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 11 | benchmark_ej11 | llama2 |  | ✓ | ✓ | ✓ | |
| 11 | benchmark_ej11 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 12 | benchmark_ej12 | llama2 | ✓ | ✓ |  | ✓ | |
| 12 | benchmark_ej12 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 13 | benchmark_ej13 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 13 | benchmark_ej13 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 14 | benchmark_ej14 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 14 | benchmark_ej14 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 15 | benchmark_ej15 | llama2 | ✓ |  | ✓ | ✓ | |
| 15 | benchmark_ej15 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 16 | benchmark_ej16 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 16 | benchmark_ej16 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 17 | benchmark_ej17 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 17 | benchmark_ej17 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 18 | benchmark_ej18 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 18 | benchmark_ej18 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 19 | benchmark_ej19 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 19 | benchmark_ej19 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 20 | benchmark_ej20 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 20 | benchmark_ej20 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 21 | benchmark_ej21 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 21 | benchmark_ej21 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 22 | benchmark_ej22 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 22 | benchmark_ej22 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 23 | benchmark_ej23 | llama2 | ✓ |  | ✓ | ✓ | |
| 23 | benchmark_ej23 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 24 | benchmark_ej24 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 24 | benchmark_ej24 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 25 | benchmark_ej25 | llama2 |  | ✓ | ✓ | ✓ | |
| 25 | benchmark_ej25 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 26 | benchmark_ej26 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 26 | benchmark_ej26 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 27 | benchmark_ej27 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 27 | benchmark_ej27 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 28 | benchmark_ej28 | llama2 | ✓ | ✓ |  | ✓ | |
| 28 | benchmark_ej28 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 29 | benchmark_ej29 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 29 | benchmark_ej29 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |
| 30 | benchmark_ej30 | llama2 | ✓ | ✓ | ✓ | ✓ | |
| 30 | benchmark_ej30 | llama3.2 | ✓ | ✓ | ✓ | ✓ | |

## 5. Conclusiones

### 5.1 Rendimiento General
- Comparativa de tiempos de respuesta entre modelos: Llama3.2 es apenas mas rapido, solo en algunas preguntas especificas tardo mas que Llama2.


### 5.2 Comparativa por Idioma
- Análisis de rendimiento en español vs inglés: Llama3.2 en Ingles obtiene las respuestas mas acertadas y tarda menos en responder.


## 6. Recomendaciones

### 6.1 Selección de Modelo
- Recomendaciones basadas en el tipo de problema: Las versiones de llama2 y 3.2 fueron seleccionadas por tener 
- Consideraciones de hardware necesarias

### 6.2 Mejores Prácticas
- Tips para optimizar prompts
- Estrategias para mejorar la precisión
- Consideraciones de rendimiento
