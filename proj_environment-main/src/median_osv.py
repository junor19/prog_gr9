import pandas as pd
import numpy as np
import sys
import os


import hente_apidata

hente_apidata.hent_solskinnstimer("t_månder","t_dager", "raa_data_m.csv")

df =pd.read_csv(os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_m.csv'))

print(df.median()) #summerer median

print(df.mean()) #summerer gjennomsnitt

print(df.std()) # finner standardavviik