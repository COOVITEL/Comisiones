import pandas as pd


def readExcel(name: str, file: str, columns: list) -> dict:
    """"""
    pf = pd.read_excel("files/Agosto.xlsx",
                       sheet_name=file,
                       usecols=columns)
    dates = pf.loc[pf["PROMOTOR"] == name].to_dict(orient="records")
    return dates
