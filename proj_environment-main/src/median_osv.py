import pandas as pd
import numpy as np
import sys
import os

import hente_apidata

hente_apidata.hent_solskinnstimer("t_månder","seksten", "raa_data_m.csv")
hente_apidata.hent_solskinnstimer("t_månder", "tjue", "raa_data_d.csv")

df_m =pd.read_csv(os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_m.csv'))
df_d =pd.read_csv(os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_d.csv'))

print("median er:", df_m.median(numeric_only=True))#summerer median

print("gjennomsnittet er:",df_m.mean(numeric_only=True))#summerer gjennomsnitt

print("standardavviket er:",df_m.std(numeric_only=True))# finner standardavviik

print("median er:", df_d.median(numeric_only=True)) #summerer median

print("gjennomsnittet er:", df_d.mean(numeric_only=True)) # summerergjennomsnittet

print("standardavviket er:", df_d.std(numeric_only=True)) #finner standardavviket