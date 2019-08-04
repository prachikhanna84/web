import pandas as pd
import csv

df = pd.read_csv("./Resources/cities.csv")
print(df)
df.to_html('./data.html',index=False)