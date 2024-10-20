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


                    # Convertir 'year_of_release' a tipo entero
df['year_of_release'] = df['year_of_release'].astype('Int64')

# Ver los valores únicos de la columna 'year_of_release'
print("Valores únicos en 'year_of_release':")
print(df['year_of_release'].unique())

# Calcular la mediana de 'year_of_release' (ignorando los valores NaN)
median_year = df['year_of_release'].median()

# Imputar los valores faltantes con la mediana
df['year_of_release'].fillna(median_year, inplace=True)

# Verificar los cambios
print("Valores únicos en 'year_of_release' después de la imputación:")
print(df['year_of_release'].unique())

# Ver las primeras filas para confirmar
print("Primeros valores en 'year_of_release' después de la imputación:")
print(df['year_of_release'].head(10))

                # Verificar si hay valores faltantes en otras columnas
print(df.isnull().sum())
print(df.dtypes)
# Eliminar filas con valores faltantes en 'name' y 'genre'
df = df.dropna(subset=['name', 'genre'])

# Imputar 'critic_score' y 'user_score' con la mediana
df['critic_score'] = df['critic_score'].fillna(df['critic_score'].median())
df['user_score'] = df['user_score'].fillna(df['user_score'].median())

# Imputar 'rating' con el valor más frecuente (moda)
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Verificar los cambios
print(df.isnull().sum())

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']] = scaler.fit_transform(df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']])

# Verificar si hay outliers en las columnas de ventas
df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].describe()

df = pd.get_dummies(df, columns=['platform'], drop_first=True)

# Calcular las ventas totales sumando las ventas en todas las regiones
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']

# Verificar el resultado mostrando las primeras filas
print(df[['name', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'total_sales']].head())



