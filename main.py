import pandas as pd

df = pd.read_json("json/prod_products_06_07_2022_11_53.json")
df = df['results']

output = pd.DataFrame()

for row in df:
    output = output.append(row, ignore_index=True)

output.to_csv("prod_products_06_07_2022_11_53.csv")