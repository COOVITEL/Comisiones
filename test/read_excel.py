#!/usr/bin/python3
import pandas as pd

def Afiliaciones(file: str):
    """"""
    df = pd.read_excel(file, 
                        sheet_name="Afiliaciones",
                        usecols=['REGIONAL', 'ACUM_APO', 'ACUM_AHO', 'PROMOTOR', 'SUBZONA', 'SUCURSAL'])
    df.to_csv('Afiliaciones_agosto.csv', index=False)

def cdat(file: str):
    cvs = pd.read_excel(file,
                        sheet_name="CDAT",
                        usecols=['REGIONAL', 'V_TITULO', 'PROMOTOR', 'SUC_PRODUCTO', 'SUC_ASOCIADO'])
    cvs.to_csv('CDATS_agosto.csv', index=False)


if __name__ == '__main__':
    Afiliaciones('Agosto.xlsx')
    cdat("Agosto.xlsx")