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

# Verificar los tipos de datos actuales
print("Tipos de datos originales:")
print(df.dtypes)

# Ver los valores únicos de la columna 'user_score'
print("Valores únicos en 'user_score':")
print(df['user_score'].unique())
    
              # Reemplazar el valor 'tbd' con NaN
df['user_score'] = df['user_score'].replace('tbd', pd.NA)

            # Convertir 'user_score' a tipo float
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# Verificar la conversión
print("Tipos de datos después de la conversión de 'user_score':")
print(df['user_score'].dtypes)

# Opcional: Ver algunos valores para confirmar la conversión
print(df['user_score'].head())
