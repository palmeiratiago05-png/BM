import pandas as pd
import yfinance as yf

def import_data():
    data_import = yf.download(
        ["AAPL","NVDA"],
        period="6d",
        interval= "15m",
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
dados_limpos.to_excel(r"C:\Users\Tiago Palmeira\Downloads\190September.xlsx")

### Data set for apple.csv https://www.kaggle.com/datasets/kalilurrahman/apple-stock-data-live-and-latest-from-ipo-date?select=Apple_stock_history.csv
### Or this site for apple https://www.kaggle.com/datasets/kalilurrahman/apple-stock-data-live-and-latest-from-ipo-date?resource=download
