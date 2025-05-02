import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))


import hente_apidata

hente_apidata.hent_solskinnstimer("t_månder","seksten", "raa_data_m.csv")
hente_apidata.hent_solskinnstimer("t_dager", "tjue", "raa_data_d.csv")

df_m =pd.read_csv(os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_m.csv'))
df_d =pd.read_csv(os.path.join(os.path.dirname(__file__),'..','data', 'raa_data_d.csv'))


print(df_m.isnull().sum()) #summerer antall som mangler i m
print(df_d.isnull().sum()) #summerer antall som mangler i d