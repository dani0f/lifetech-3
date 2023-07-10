import csv
import numpy as np

def cargar_embeddings_desde_csv(ruta_archivo):
    embeddings = []
    with open(ruta_archivo, 'r') as archivo_csv:
        reader = csv.reader(archivo_csv)
        next(reader)  # Omitir la primera fila de encabezados

        for row in reader:
            embedding = np.array(row, dtype=np.float32)
            embeddings.append(embedding)

    return embeddings


