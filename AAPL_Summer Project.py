import pandas as pd
import yfinance as yf

df = yf.download(
    "AAPL",
    period="6d",
    interval="1m",  
    progress= False
)
###df.index = df.index.tz_localize('None') ### Verificar como deveria atingir isto
print(df)
df.to_excel("Apple_stock_excel_teste3.xlsx")
