import pandas as pd
import numpy as np
import sys
import os
import csv


def statistikk(filnavn):

    df_d =pd.read_csv(filnavn) #leser CVSen
    median = df_d.median(numeric_only=True) #regner ut median
    gjennomsnitt = df_d.mean(numeric_only=True) #regner ut gjennomsnitt
    standardavvik = df_d.std(numeric_only=True) #regner ut standardavvik
    return median, gjennomsnitt, standardavvik #returnerer median, gjennomsnitt og standardavvik 

if __name__ == "__main__":
    
    filbane = os.path.join(os.path.dirname(__file__),'..', 'data', 'utfylt_data.csv')# lager filbane til csv-filen
    median, gjennomsnitt, standardavvik = statistikk(filbane) #kaller på funksjonen og sender inn filbane
    print("median er:", median) #summerer median
    print("gjennomsnittet er:", gjennomsnitt) # summerergjennomsnittet
    print("standardavviket er:", standardavvik) #finner standardavviket
    
    
'''
W3Schools. (n.d.-a). *Pandas median, gjennomsnitt, standardavvik.* www.w3school.com. https://www.w3schools.com/python/pandas/ref_df_median.asp

openAI(n.d.-a). *Chatgpt (GPT-4).* https://chatgpt.com/
'''