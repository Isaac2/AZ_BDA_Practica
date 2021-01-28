import pandas

data_logs = pandas.read_csv("../datasets/censo_poblacion_2020.csv")
#print(data_logs.shape)

#Aquí observamos que tienen errores las columnas 1995 y 2000
#print(data_logs.info())
#print(data_logs.dtypes)

data_logs["indicador"] = data_logs["indicador"].astype('string')
data_logs["1995"] = pandas.to_numeric(data_logs["1995"], errors="coerce").fillna(0)
data_logs["2000"] = pandas.to_numeric(data_logs["2000"], errors="coerce").fillna(0)
data_logs["2015"] = pandas.to_numeric(data_logs["2015"], errors="coerce").fillna(0)
data_logs["2020"] = pandas.to_numeric(data_logs["2020"], errors="coerce").fillna(0)
data_logs["unidad_medida"] = data_logs["unidad_medida"].astype('string')

#FIXED
#print(data_logs.info())
#print(data_logs.dtypes)

#Valores únicos
#print( data_logs["desc_entidad"].value_counts() )

#indicador es el nombre del estado
#edad_medianas_estado = data_logs.loc[ data_logs["indicador"] == "Edad mediana", ["desc_entidad", "2020"]]
#print( edad_medianas_estado.shape )

#Promedio ordenados por estado
#edad_medianas_estado = data_logs.loc[ data_logs["indicador"] == "Edad mediana", ["desc_entidad", "2020"] ]
#print( edad_medianas_estado.groupby("desc_entidad")["2020"].mean() )

#Actividad
#edad_medianas_estado = data_logs.loc[ data_logs["indicador"] == "Edad mediana", ["desc_entidad", "2015", "2020"] ]
#edad_medianas_estado["diferencia"] = edad_medianas_estado["2020"] - edad_medianas_estado["2015"]
#print( edad_medianas_estado.shape )
#edad_medianas_estado = edad_medianas_estado[ edad_medianas_estado["diferencia"] != 0 ]
#print( edad_medianas_estado.shape )
#print( edad_medianas_estado.groupby("desc_entidad", sort=True ).mean() )

#edad_medianas_estado.to_csv("diferencias_edades_estado.csv")
#edad_medianas_estado.groupby("desc_entidad", sort=True ).mean().to_csv("diferencias_edades_estado.csv")