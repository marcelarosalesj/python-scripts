# Data retrived from https://data.cic.mx/Poblaci-n/Homicidios-en-NL-1990-2010-INEGI-Estad-sticas-vita/ayuk-9x69
#

import numpy as np
import urllib
import logging
import pandas as pd
import re

# Get the data.
df=pd.read_csv("Percepcion_Seguridad_Parte.csv", sep=',' , encoding='utf-8' )

# Cleaning
for i in range(0, df.shape[0]):
    # Cleaning column 3. It works.
    aux = re.search("[0-9]+\-[0-9]+", df.loc[i, "GRUPOEDAD"])
    if aux == None:
        print "NONE"
        df.loc[i, "GRUPOEDAD"] = "0"
    else:
        print df.loc[i, "GRUPOEDAD"][aux.start(): aux.end()]
        df.loc[i, "GRUPOEDAD"] = df.loc[i, "GRUPOEDAD"][aux.start(): aux.end()]
    # Cleaning column 6. Garcia, Juarez...
    if df.loc[i, "MUNICIPIO"][0:2] == "Ga":
        df.loc[i, "MUNICIPIO"] = "Garcia"
    elif df.loc[i, "MUNICIPIO"][0:2] == "Ju":
        df.loc[i, "MUNICIPIO"] = "Juarez"

print df
