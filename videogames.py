import pandas as pd

# Cargar el dataset desde la carpeta 'videogames'
file_path = './videogames/games.csv'
df = pd.read_csv(file_path)

# Verificar las columnas antes de modificarlas
print("Columnas originales:")
print(df.columns)

# Reemplazar los nombres de las columnas y ponerlas en minúsculas
df.columns = df.columns.str.lower()

# Verificar las columnas después de la modificación
print("Columnas modificadas:")
print(df.columns)