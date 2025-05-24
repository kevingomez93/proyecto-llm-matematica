# Evaluación Comparativa de Modelos LLM

## Configuración de la prueba

- **Fecha:** 24/05/2025 15:33
- **Modelos probados:** llama2, llama3.2
- **Número de problemas:** 2
- **Especificaciones de hardware:** 
  - CPU: arm
  - RAM: 16.0 GB
  - VRAM: 16.0 GB (unified memory with RAM)
  - GPU: Apple M2 Pro
  - Sistema: Darwin 24.4.0

## Resultados de tiempos

| Problema | llama2 (ms) | llama3.2 (ms) | Diferencia (ms) | Diferencia (%) |
|----------|---------------|---------------|---------------|---------------|
| Ejercicio 1 | 7013 | 3111 | 3902 | 125.4% |
| Ejercicio 16 | 4642 | 5403 | -761 | -14.1% |
| **Promedio** | 5827.5 | 4257.0 | 1570.5 | 55.6% |

## Evaluación de calidad

### Criterios de evaluación
- **Correcto:** La respuesta es matemáticamente correcta.
- **Paso a paso:** La respuesta explica el proceso de solución de forma clara.
- **Notación:** La respuesta utiliza notación matemática adecuada.
- **Completo:** La respuesta aborda todos los aspectos del problema.

| # | Problema | Descripción | llama2 | llama3.2 | Notas |
|---|----------|-------------|----------|----------|-------|
| 1 | Probabilidad dados | Calcular probabilidad de suma 7 al tirar dos dados | |  |  |
| 16 |  |  | |  |  |

## Conclusiones

[Enumerar las conclusiones principales sobre el rendimiento de los modelos]

## Recomendaciones

[Recomendaciones sobre qué modelo utilizar para diferentes tipos de problemas]