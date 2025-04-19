import pandas as pd
import numpy as np
import sys
import os

src_path=sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(src_path)

import hente_apidata

hente_apidata.hent_solskinnstimer("t_månder","seksten", "raa_data_m.csv")

df =pd.read_csv(os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_m.csv'))


print(df.isnull().sum())