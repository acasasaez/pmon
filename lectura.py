import pandas as pd 
import numpy 

df = pd.read_csv(r"Pokemon.csv")
af = pd.read_csv(r"Pokemon.csv")
bf = pd.read_csv(r"Pokemon.csv")
cf = pd.read_csv(r"Pokemon.csv")
ef = pd.read_csv(r"Pokemon.csv")
hf = pd.read_csv(r"Pokemon.csv")
print(df)
af = af[["Attack"]]
df = df[["Speed"]]
bf = af[["Defense"]]
ef = af[["Sp. Atk"]]
hf =hf[["Attack"]]

print(df.head())