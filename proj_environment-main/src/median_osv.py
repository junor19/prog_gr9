import pandas as pd
import numpy as np
import sys
import os

def statistikk(filnavn):

    df_d =pd.read_csv(filnavn) #leser CVSen
    median = df_d.median(numeric_only=True) #regner ut median
    gjennomsnitt = df_d.mean(numeric_only=True) #regner ut gjennomsnitt
    standardavvik = df_d.std(numeric_only=True) #regner ut standardavvik
    return median, gjennomsnitt, standardavvik #returnerer median, gjennomsnitt og standardavvik 

if __name__ == "__main__":
    import hente_apidata
    hente_apidata.hent_solskinnstimer("t_månder", "tjue", "raa_data_d.csv") #henter data fra API
    
    filbane = os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_d.csv')# lager filbane
    median, gjennomsnitt, standardavvik = statistikk(filbane) #kaller på funksjonen og sender inn filbane
=======
    df_d =pd.read_csv(filnavn)
    median = df_d.median(numeric_only=True)
    gjennomsnitt = df_d.mean(numeric_only=True)
    standardavvik = df_d.std(numeric_only=True)
    return median, gjennomsnitt, standardavvik

if __name__ == "__main__":
    import hente_apidata
    hente_apidata.hent_solskinnstimer("t_månder", "tjue", "raa_data_d.csv")
    
    filbane = os.path.join(os.path.dirname(__file__),'..', 'data', 'raa_data_d.csv')
    median, gjennomsnitt, standardavvik = statistikk(filbane)


print("median er:",median) #summerer median
print("gjennomsnittet er:", gjennomsnitt) # summerergjennomsnittet
print("standardavviket er:", standardavvik) #finner standardavviket