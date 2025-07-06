from google colab import files
uploaded = files.upload()
corpus_file_path = list(uloaded.keys())[0]
print ("Archivo cargado: ", corpus_file_path)
import pandas as pd
import numpy as np

# Cargar el corpus original desde texto
def cargar_corpus(file_path):
    corpus = []
    with open(file_path, "r", encoding="utf-8") as file:
        documento = []
        for linea in file:
            linea = linea.strip()
            if linea.startswith("<doc"):
                continue  # Ignorar líneas de inicio de documentos
            elif linea == "":  # Saltar líneas vacías
                continue
            else:
                datos = linea.split("\t")
                corpus.append((datos[0], datos[2]))  # Extraer token y etiqueta POS
    return corpus

# Cargar el corpus
file_path = "./corpus_etiquetado.txt"  # Cambia esto a la ruta de tu archivo
corpus = cargar_corpus(file_path)
print("Paso 1: Corpus cargado con éxito.")

# Calcular las probabilidades de emisión
def calcular_prob_emision(corpus):
    emision = {}
    total_etiquetas = {}
    for token, etiqueta in corpus:
        if etiqueta not in emision:
            emision[etiqueta] = {}
            total_etiquetas[etiqueta] = 0
        emision[etiqueta][token] = emision[etiqueta].get(token, 0) + 1
        total_etiquetas[etiqueta] += 1

    prob_emision = {
        etiqueta: {token: freq / total_etiquetas[etiqueta] for token, freq in tokens.items()}
        for etiqueta, tokens in emision.items()
    }
    return prob_emision

prob_emision = calcular_prob_emision(corpus)
print("Paso 2: Probabilidades de emisión calculadas.")

# Calcular las probabilidades de transición, incluyendo estado inicial (<s>)
def calcular_prob_transicion(corpus):
    transicion = {}
    total_transiciones = {}

    etiquetas = [etiqueta for _, etiqueta in corpus]

    # Calcular transiciones desde el estado inicial (<s>)
    transicion["<s>"] = {}
    for etiqueta in etiquetas[:1]:  # Solo las primeras etiquetas de las frases
        transicion["<s>"][etiqueta] = transicion["<s>"].get(etiqueta, 0) + 1

    # Normalizar las transiciones desde <s>
    total_inicial = sum(transicion["<s>"].values())
    transicion["<s>"] = {etiqueta: freq / total_inicial for etiqueta, freq in transicion["<s>"].items()}

    # Calcular transiciones entre etiquetas
    for i in range(1, len(etiquetas)):
        prev_etiqueta = etiquetas[i - 1]
        curr_etiqueta = etiquetas[i]
        if prev_etiqueta not in transicion:
            transicion[prev_etiqueta] = {}
            total_transiciones[prev_etiqueta] = 0
        transicion[prev_etiqueta][curr_etiqueta] = transicion[prev_etiqueta].get(curr_etiqueta, 0) + 1
        total_transiciones[prev_etiqueta] += 1

    # Normalizar las transiciones
    for prev_etiqueta in total_transiciones:
        transicion[prev_etiqueta] = {
            curr_etiqueta: freq / total_transiciones[prev_etiqueta]
            for curr_etiqueta, freq in transicion[prev_etiqueta].items()
        }

    return transicion

prob_transicion = calcular_prob_transicion(corpus)
print("Paso 3: Probabilidades de transición calculadas.")

# Guardar las probabilidades en Excel
prob_emision_df = pd.DataFrame(prob_emision).fillna(0)
prob_transicion_df = pd.DataFrame(prob_transicion).fillna(0)
prob_emision_df.to_excel("probabilidades_emision.xlsx", index=True)
prob_transicion_df.to_excel("probabilidades_transicion.xlsx", index=True)
print("Paso 4: Probabilidades de emisión y transición guardadas en Excel.")

# Algoritmo de Viterbi
def viterbi(oracion, estados, prob_emision, prob_transicion, inicio="<s>", final="</s>"):
    n = len(oracion)
    m = len(estados)
    viterbi_matrix = np.zeros((m, n))
    backpointer = np.zeros((m, n), dtype=int)

    # Inicialización
    for i, estado in enumerate(estados):
        viterbi_matrix[i, 0] = prob_transicion.get(inicio, {}).get(estado, 1e-6) * prob_emision.get(estado, {}).get(oracion[0], 1e-6)

    # Recursión
    for t in range(1, n):
        for i, estado_actual in enumerate(estados):
            max_prob = 0
            best_prev_state = 0
            for j, estado_anterior in enumerate(estados):
                prob = viterbi_matrix[j, t-1] * prob_transicion.get(estado_anterior, {}).get(estado_actual, 1e-6) * prob_emision.get(estado_actual, {}).get(oracion[t], 1e-6)
                if prob > max_prob:
                    max_prob = prob
                    best_prev_state = j
            viterbi_matrix[i, t] = max_prob
            backpointer[i, t] = best_prev_state

    # Terminación
    best_path = [0] * n
    best_path[-1] = np.argmax(viterbi_matrix[:, -1])
    for t in range(n-2, -1, -1):
        best_path[t] = backpointer[best_path[t+1], t+1]
    best_sequence = [estados[i] for i in best_path]

    return best_sequence, viterbi_matrix

# Definir la oración
oracion = ["Habla", "con", "el", "enfermo", "grave", "de", "trasplantes", "."]
estados = list(prob_emision.keys())

# Ejecutar Viterbi
mejor_secuencia, viterbi_matrix = viterbi(oracion, estados, prob_emision, prob_transicion)
print("Paso 5: Algoritmo de Viterbi ejecutado.")

# Guardar la matriz de Viterbi en Excel
viterbi_df = pd.DataFrame(viterbi_matrix, index=estados, columns=oracion)
viterbi_df.to_excel("viterbi_matrix.xlsx", index_label="Estado")
print("Paso 6: Matriz de Viterbi guardada en Excel.")

# Imprimir la oración etiquetada
oracion_etiquetada = list(zip(oracion, mejor_secuencia))
print("Oración etiquetada:", oracion_etiquetada)
