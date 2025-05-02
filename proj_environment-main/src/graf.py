import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

import hente_apidata
import variabler

hente_apidata.hent_solskinnstimer("t_dager", "tjue", "raa_data_d.csv")
df_d =pd.read_csv(os.path.join(os.path.dirname(__file__),'..','data', 'raa_data_d.csv'))

data = pd.read_csv("hente_apidata")

print(data.head())