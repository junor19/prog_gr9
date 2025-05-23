import pandas as pd
import numpy as np
import sys
import os

import hente_apidata

hente_apidata.hent_solskinnstimer("t_dager", "tjue", "raa_data_d.csv")

df_d =pd.read_csv(os.path.join(os.path.dirname(__file__),'..','data', 'raa_data_d.csv'))

print(df_d.isnull().sum()) #summerer og sjekker manglende verdier
