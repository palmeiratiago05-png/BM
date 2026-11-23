import pandas as pd
import yfinance as yf

def import_data():
    data_import = yf.download(
        ["VTI","VEA","VWO","BND","GLD","VNQ","SPY","QQQ","EZU","MCHI"],
        start="2007-01-01",
        end="2026-11-21",
        interval= "1d",
        group_by="ticker"
    )
    data_import.index = data_import.index.tz_localize(None)   # agora afeta o df que realmente vais gravar

    return data_import

def clean_data(import_data):
    cleaner = import_data.dropna()
    return cleaner


## Conectar os dados 
dados_brutos = import_data()
dados_limpos = clean_data(dados_brutos)
print(dados_limpos)
dados_limpos.to_csv("190September.csv")
    ####(r"C:\Users\____\Downloads\190September.csv")

