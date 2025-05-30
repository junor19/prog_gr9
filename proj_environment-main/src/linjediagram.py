import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

import sentralmal
from sentralmal import statistikk

# Forbereder og laster inn data fra CSV-fil
def laste_data():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv') #filsti til csv
    df = pd.read_csv(path) #leser csv filen
    df['date'] = pd.to_datetime(df['date']) #konverterer datoen til datetime format
    df['year'] = df['date'].dt.year #henter ut året fra datoen og legger i egen kolonne
    df['day_month'] = df['date'].dt.strftime('%m-%d') #henter ut dag og måned fra datoen og legger i egen kolonne
    return df, path

#
def lage_graf(df, median=None, gjennomsnitt=None):
    #lager tabell for dag og månder, verdi er solskinnstimer
    pivot_df = df.pivot(index='day_month', columns='year', values='sunshine_hours').sort_index() 
    
    plt.figure(figsize=(20, 6)) #størresle 
    for year in pivot_df.columns: #lager linje for hvert år
        plt.plot(pivot_df.index, pivot_df[year], label=str(year), alpha=0.7) #tegner linje for hvert år
        
    if median is not None: #hvis median er gitt
        plt.axhline(median, color='black', linestyle='--', label='Median')
    if gjennomsnitt is not None: #hvis gjennomsnitt er gitt
        plt.axhline(gjennomsnitt, color='grey', linestyle='--', label='Gjennomsnitt')
        
        
    plt.title('Solskinnstimer per dag og måned') #tittel på grafen
    plt.xlabel('Dag-Måned') #x-akse
    plt.ylabel('Solskinnstimer') #y-akse
    plt.xticks(rotation=45) #roterer x-aksen for bedre lesbarhet
    plt.legend() #legger til legende
    plt.tight_layout() #rydder opp i layouten
    plt.show() #viser grafen
    return pivot_df #returnerer tabellen med dataene
    
if __name__ == "__main__":
    df, path = laste_data() #leser csv, konverterer datoen til datetime format
    median, gjennomsnitt,_ = statistikk(path) #henter median og gjennomsnitt fra statistikk funksjonen
    
    lage_graf(
        df, 
        median=median['sunshine_hours'],
        gjennomsnitt=gjennomsnitt['sunshine_hours']
    ) # lager grafen med median og gjennomsnitt
    
    
'''
Matplotlib. (n.d.-a). *matplotlib Plotting categorical variables.* www.matplotlib.org. https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py

Matplotlib. (n.d.-a). *Matplotlib constrained layout quide.* www.matplotlib.org. https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html    

Geeksforgeeks. (n.d.-a). *Geeksforgeeks linechart in Matplotlib-Python.* www.Geeksforgeeks.org. https://www.geeksforgeeks.org/line-chart-in-matplotlib-python/

openAI(n.d.-a). *Chatgpt (GPT-4).* https://chatgpt.com/

Python. (n.d.-a). *Python matplotlib line linestyle.* www.python.org. https://www.w3schools.com/python/matplotlib_line.asp
'''
    