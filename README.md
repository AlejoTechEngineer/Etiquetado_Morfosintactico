# Etiquetador Morfosintáctico (POS Tagger) con HMM

![NLP](https://img.shields.io/badge/NLP-POS_Tagging-00897B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HMM](https://img.shields.io/badge/HMM-Viterbi-8E24AA?style=for-the-badge)

> POS tagger con Modelo Oculto de Markov implementado desde cero: entrenamiento supervisado y decodificación Viterbi.

## Descripción

Implementación completa de un etiquetador morfosintáctico (Part-of-Speech Tagger) basado en **Modelos Ocultos de Markov (HMM)** construido desde cero en Python/Jupyter. Incluye estimación de probabilidades de emisión y transición sobre corpus etiquetado, decodificación con el algoritmo de **Viterbi** y evaluación de precisión por categoría gramatical.

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `analizador_HMM_desde_cero_funcional.ipynb` | Implementación base del HMM POS tagger |
| `analizador_HMM_desde_cero_funcional_mejorado.ipynb` | Versión optimizada con suavizado y manejo de OOV |
| `corpus_etiquetado.txt` | Corpus de entrenamiento y evaluación |
| `*.pdf` | Informe de resultados y análisis |

## Arquitectura del HMM

```
Estados ocultos: etiquetas POS (NOUN, VERB, ADJ, ...)
Observaciones: palabras del texto
π: probabilidad inicial de cada etiqueta
A: matriz de transición entre etiquetas
B: matriz de emisión (P(palabra|etiqueta))

Decodificación: Algoritmo de Viterbi en O(N²T)
```

## Contexto académico

**Asignatura:** Minería de Información y Análisis — NLP · **Institución:** Ingeniería Informática
**Autor:** Alejandro De Mendoza — Ingeniero Informático · Especialista en IA
