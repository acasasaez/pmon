# pmon
Para esta prueba se nos ha dado un dataset con pokemon. 

He importado este archivo a python. 

Con Pandas he hecho una lectura del archivo. 

Con Numpy he calculado la media, mediana, desviación típica y varianza  de Velocidad, Fuerza de defensa y ataque, Rango de soporte de defensa y ataque y poder de los pokemon. 

 He creado un archivo csv que recibiese los resultados calculados mediante numpy. 
 
 Finalmente, he importado el ejercicio inicial del examen con intención de modificarlo. 
 
 

### CÓDIGO HECHO PARA ESTE EXAMEN: 

```
import pandas as pd 
import numpy 

df = pd.read_csv(r"Pokemon.csv")
af = pd.read_csv(r"Pokemon.csv")
bf = pd.read_csv(r"Pokemon.csv")
cf = pd.read_csv(r"Pokemon.csv")
ef = pd.read_csv(r"Pokemon.csv")
hf = pd.read_csv(r"Pokemon.csv")
lf = pd.read_csv(r"Pokemon.csv")
print(df)

af = af[["Attack"]]
df = df[["Speed"]]
bf = bf[["Defense"]]
ef = ef[["Sp. Atk"]]
hf =hf[["Sp. Def"]]
lf = lf[["HP"]]
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


Media_spd = np.mean(hf)
Mediana_spd = np.median(hf)
Desviacion_spd = np.std(hf)
Varianza_spd = np.var(hf)

Media_hp = np.mean(lf)
Mediana_hp = np.median(lf)
Desviacion_hp = np.std(lf)
Varianza_hp = np.var(lf)
datos = [
    [Media_Velocidad, Mediana_Velocidad, Desviacion_Velocidad, Varianza_Velocidad],
[Media_Ataque, Mediana_Ataque, Desviacion_Ataque, Varianza_Ataque],
[Media_defensa, Mediana_defensa, Desviacion_defensa, Varianza_defensa], 
[Media_spa, Mediana_spa, Desviacion_spa, Varianza_spa], 
[Media_spd, Mediana_spd, Desviacion_spd, Varianza_spd],
[Media_hp, Mediana_hp, Desviacion_hp, Varianza_hp]]

import csv
with open("resultados.csv.csv", "w",newline = "") as file: 
    writer =csv.writer(file, delimiter = "," )
    writer.writerow( ["TABLA DE DATOS RESULTADOS"])
    writer.writerows(datos)

```
