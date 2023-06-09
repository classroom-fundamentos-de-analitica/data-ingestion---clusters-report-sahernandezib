"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    i = 0
    dict1 = {}
    df = pd.DataFrame()
    with open('./clusters_report.txt') as f:
        for line in f:
            

            line = re.sub(r"\s+", " ", line)
            if len(line)>1 and i > 3:
                if line.split()[0].isnumeric() == True:
                    try: 
                        dict1['principales_palabras_clave'] = ' '.join(dict1['principales_palabras_clave'])
                        df = df.append(dict1, ignore_index=True)
                    except: pass
                    dict1 = {'cluster': int(line.split()[0]),
                                'cantidad_de_palabras_clave': int(line.split()[1]),
                                'porcentaje_de_palabras_clave': float(line.split()[2].replace(',','.')),
                                'principales_palabras_clave': line.split()[4:]}
                else: 
                    dict1['principales_palabras_clave'].append(' '.join(line.split()))
            i += 1
    dict1['principales_palabras_clave'] = ' '.join(dict1['principales_palabras_clave'])
    df = df.append(dict1, ignore_index=True)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.rstrip('\.')

    return df
