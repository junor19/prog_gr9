import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

import sentralmal
from sentralmal import statistikk


# ---------- STEG 1: Kjør full datapipeline ----------
def forbered_og_last_data():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv') #filsti til csv
    path = os.path.normpath(path) #rydder stien sjekker at det er rett format
    df = pd.read_csv(path) #leser csv filen
    df['date'] = pd.to_datetime(df['date']) #konverterer datoen til datetime format
    df['year'] = df['date'].dt.year #henter ut året fra datoen og legger i egen kolonne
    df['day_month'] = df['date'].dt.strftime('%m-%d') #henter ut dag og måned fra datoen og legger i egen kolonne
    return df

# ---------- STEG 2: Lag daglig sammenligningsgraf ----------
def lag_daglig_graf(df, median=None, gjennomsnitt=None):
    #lager tabell for dag og månder, verdi er solskinnstimer
    pivot_df = df.pivot(index='day_month', columns='year', values='sunshine_hours').sort_index() 

    plt.figure(figsize=(20, 6)) #størresle 
    for year in pivot_df.columns: #lager linje for hvert år
        plt.plot(pivot_df.index, pivot_df[year], label=str(year), alpha=0.7) #tegner linje for hvert år

#sjekker om median er en float
    if isinstance(median, (int, float, np.number, pd.Series)) and not isinstance(median, pd.Series):
        #hvis er enkeltverdi, tegner horisontal linje
        plt.axhline(median, color='black', linestyle='--', linewidth=2, label=f"Total median ({median:.2f})")
        #hvis det er en serie, tegner linje for median per dag
    elif isinstance(median, pd.Series):
        plt.plot(median.index, median.values, label='Median per dag', color='black', linestyle='--', linewidth=2)
#sjekker om gjennomsnitt er en float
    if isinstance(gjennomsnitt, (int, float, np.number, pd.Series)) and not isinstance(gjennomsnitt, pd.Series):
        #hvis er enkeltverdi, tegner horisontal linje
        plt.axhline(gjennomsnitt, color='grey', linestyle='--', linewidth=2, label=f"Total gj.snitt ({gjennomsnitt:.2f})")
        #hvis det er en serie, tegner linje for gjennomsnitt per dag
    elif isinstance(gjennomsnitt, pd.Series):
        plt.plot(gjennomsnitt.index, gjennomsnitt.values, label='Gj.snitt per dag', color='grey', linestyle='--', linewidth=2)



    plt.title("Daglig solskinn (timer) – sammenlignet per år")
    plt.xlabel("Dato (mm-dd)")
    plt.ylabel("Solskinnstimer")
    plt.legend(title="År")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return pivot_df  # returneres så den kan brukes videre


if __name__ == "__main__":
    df = forbered_og_last_data() #leser csv, konverterer datoen til datetime format
    
    # Lag pivot-tabell som i funksjonen for å regne statistikk per dag/måned
    df['year'] = df['date'].dt.year #henter ut årstallet
    df['day_month'] = df['date'].dt.strftime('%m-%d') #henter ut dag og måned
    pivot_df = df.pivot(index='day_month', columns='year', values='sunshine_hours').sort_index() #lager pivot-tabell
    median, gjennomsnitt,_=statistikk(os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv')) #henter median og gjennomsnitt fra statistikk-funksjonen

    filbane = os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv') #lager filbane til csv
    median_verdi = median['sunshine_hours'] #henter median verdien fra median tabellen
    gjennomsnitt_verdi = gjennomsnitt['sunshine_hours'] #henter gjennomsnitt verdien fra gjennomsnitt tabellen
    
    lag_daglig_graf(df, median=median_verdi, gjennomsnitt=gjennomsnitt_verdi)