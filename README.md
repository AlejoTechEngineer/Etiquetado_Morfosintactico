<div align="center">

# Etiquetador Morfosintáctico (POS Tagger) con HMM

![NLP](https://img.shields.io/badge/NLP-POS_Tagging-00897B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HMM](https://img.shields.io/badge/HMM-Viterbi-8E24AA?style=for-the-badge)

> POS tagger con Modelo Oculto de Markov implementado desde cero: entrenamiento supervisado y decodificación Viterbi.

## Descripción

</div>

---

Implementación completa de un etiquetador morfosintáctico (Part-of-Speech Tagger) basado en **Modelos Ocultos de Markov (HMM)** construido desde cero en Python/Jupyter. Incluye estimación de probabilidades de emisión y transición sobre corpus etiquetado, decodificación con el algoritmo de **Viterbi** y evaluación de precisión por categoría gramatical.

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `analizador_HMM_desde_cero_funcional.ipynb` | Implementación base del HMM POS tagger |
| `analizador_HMM_desde_cero_funcional_mejorado.ipynb` | Versión optimizada con suavizado y manejo de OOV |
| `corpus_etiquetado.txt` | Corpus de entrenamiento y evaluación |
| `*.pdf` | Informe de resultados y análisis |

## Arquitectura

```mermaid
flowchart TD
    A[corpus_etiquetado.txt - Corpus de entrenamiento] --> B[Estimar probabilidades de emision y transicion]
    B --> C[probabilidades_emision.xlsx - P-palabra dado etiqueta]
    B --> D[probabilidades_transicion.xlsx - P-etiqueta dado etiqueta anterior]
    C & D --> E[HMM: estados ocultos = etiquetas POS]
    E --> F{Notebook}
    F --> G[analizador_HMM_desde_cero_funcional.ipynb - Version base]
    F --> H[analizador_HMM_desde_cero_funcional_mejorado.ipynb - Con suavizado OOV]
    G & H --> I[Algoritmo de Viterbi - O-N2 x T]
    I --> J[viterbi_matrix.xlsx - Matriz de decodificacion]
    J --> K[scriptmorfo3.py - Script de evaluacion]
    K --> L[Precision por categoria gramatical]
```

## Contexto académico

**Asignatura:** Minería de Información y Análisis — NLP · **Institución:** Ingeniería Informática
**Autor:** Alejandro De Mendoza — Ingeniero Informático · Especialista en IA

---

## Autor

**Alejandro De Mendoza**  
Ingeniero Informático · Especialista en IA · Especialista en Ingeniería de Software · Máster en Arquitectura de Software

[![GitHub](https://img.shields.io/badge/GitHub-AlejoTechEngineer-181717?style=for-the-badge&logo=github)](https://github.com/AlejoTechEngineer)
