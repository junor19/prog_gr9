import os
import pandas as pd
import matplotlib.pyplot as plt
from hente_apidata import hent_solskinnstimer
from finne_mangler import vasket_data

# ---------- STEG 1: Kjør full datapipeline ----------
def forbered_og_last_data():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv')
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df

# ---------- STEG 2: Lag daglig sammenligningsgraf ----------
def lag_daglig_graf(df):
    df['year'] = df['date'].dt.year #henter ut året fra datoen og legger i egen kolonne
    df['day_month'] = df['date'].dt.strftime('%m-%d') #henter ut dag og måned fra datoen og legger i egen kolonne
    #lager tabell for dag og månder, verdi er solskinnstimer
    pivot_df = df.pivot(index='day_month', columns='year', values='sunshine_hours').sort_index() 

    plt.figure(figsize=(12, 6)) #størresle 
    for year in pivot_df.columns: #lager linje for hvert år
        plt.plot(pivot_df.index, pivot_df[year], label=str(year))

    plt.title("Daglig solskinn (timer) – sammenlignet per år")
    plt.xlabel("Dato (mm-dd)")
    plt.ylabel("Solskinnstimer")
    plt.legend(title="År")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return pivot_df  # returneres så den kan brukes videre


# ---------- Kjør alt ----------
if __name__ == "__main__":
    df = forbered_og_last_data()
    lag_daglig_graf(df)