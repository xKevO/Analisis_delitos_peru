import pandas as pd
import os

# Ruta local en tu Mac donde tienes los archivos CSV
folder_path = r'C:\Users\Workspace2\Criminalidad_peru\Analisis_delitos_peru'

# Lista de archivos CSV
file_names = ['delitos_2019.csv', 'delitos_2020.csv', 'delitos_2021.csv', 'delitos_2022.csv', 'delitos_2023.csv']

# Crear una lista vacía para almacenar cada DataFrame
dataframes = []

# Cargar y agregar cada archivo CSV en la lista
for file in file_names:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Concatenar todos los DataFrames en uno solo
df_delitos = pd.concat(dataframes, ignore_index=True)

# Ver las primeras filas para confirmar la unión
df_delitos.head()