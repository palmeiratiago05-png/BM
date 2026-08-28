import pandas as pd
import numpy as np

apple_stock = pd.read_csv("Apple_stock_history.csv")
appl = apple_stock
appl = appl["Open"].agg(["mean","sum","max","min"])

### Full display
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(appl)

### Data set for apple.csv https://www.kaggle.com/datasets/kalilurrahman/apple-stock-data-live-and-latest-from-ipo-date?select=Apple_stock_history.csv
### Or this site for apple https://www.kaggle.com/datasets/kalilurrahman/apple-stock-data-live-and-latest-from-ipo-date?resource=download
