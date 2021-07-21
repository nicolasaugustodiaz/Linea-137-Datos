import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

llamados_df=pd.read_csv("datoscsv/llamados12-2020.csv")

#print(llamados_df.columns)                                         # devuelve el nombre de cada columna
#print(llamados_df.dtypes)                                          # devuelve los tipos de datos de cada columna
#print(pd.unique(llamados_df["victima_vinculo_agresor"]))           # devuelve los distintos valores que tiene la columna

data_agrupada = llamados_df.groupby("victima_genero")               # Estadistica de genéro de las víctimas x cada llamado
print(data_agrupada.describe())

