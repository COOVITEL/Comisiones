#!/usr/bin/python3
import pandas as pd

def filtered_sucursal(file: str, name: str):
    """"""
    df = pd.read_csv(file)
    sucursal = df.loc[df['REGIONAL'] == name]
    value_sucursal = sucursal['V_TITULO'].sum()
    print(value_sucursal)


def filtered_promotor(file: str, name: str):
    fil = pd.read_csv(file)
    name = fil.loc[fil["PROMOTOR"] == name]
    print(name)
    value_name = name['V_TITULO'].sum()
    print(value_name)

if __name__ == '__main__':
    filtered_sucursal("CDATS_agosto.csv", "Bogota")
    filtered_promotor("CDATS_agosto.csv", "TARAZONA TARAZONA JOHANNA MARCELA")   
    filtered_promotor("CDATS_agosto.csv", "RINCON ARROYO BRIGITTE LORENA")
    