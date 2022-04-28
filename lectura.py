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
bf = bf[["Defense"]]
ef = ef[["Sp. Atk"]]
hf =hf[["Sp. Def"]]

print(af.head())

import numpy as np
Media_Velocidad = np.mean(df)
Mediana_Velocidad = np.median(df)
Desviacion_Velocidad= np.std(df)
Varianza_Velocidad = np.var(df)

Media_Ataque = np.mean(af)
Mediana_Ataque = np.median(af)
Desviacion_Ataque = np.std(af)
Varianza_Ataque = np.var(af)

Media_defensa = np.mean(bf)
Mediana_defensa = np.median(bf)
Desviacion_defensa = np.std(bf)
Varianza_defensa = np.var(bf)

Media_spa = np.mean(ef)
Mediana_spa = np.median(ef)
Desviacion_spa = np.std(ef)
Varianza_spa = np.var(ef)


Media_spd = np.mean(df)
Mediana_spd = np.median(df)
Desviacion_spd = np.std(df)
Varianza_spd = np.var(df)


