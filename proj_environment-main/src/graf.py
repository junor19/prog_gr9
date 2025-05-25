import os
import pandas as pd
import matplotlib.pyplot as plt
from hente_apidata import hent_solskinnstimer
from finne_mangler import vasket_data

# ---------- STEG 1: Kjør full datapipeline ----------
def forbered_og_last_data():
    print("🔄 Henter og vasker data...")
    hent_solskinnstimer("t_dager", "seksten", "raa_data_d.csv")
    vasket_data("../data/raa_data_d.csv", "date")  # Lager utfylt_data.csv
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'utfylt_data.csv')
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df

# ---------- STEG 2: Lag daglig sammenligningsgraf ----------
def lag_daglig_graf(df):
    df['year'] = df['date'].dt.year
    df['day_month'] = df['date'].dt.strftime('%m-%d')
    pivot_df = df.pivot(index='day_month', columns='year', values='sunshine_hours').sort_index()

    plt.figure(figsize=(12, 6))
    for year in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[year], label=str(year))

    plt.title("Daglig solskinn (timer) – sammenlignet per år")
    plt.xlabel("Dato (mm-dd)")
    plt.ylabel("Solskinnstimer")
    plt.legend(title="År")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return pivot_df  # returneres så den kan brukes videre

# ---------- STEG 3: Se spesifikk dato over flere år ----------
def vis_solskinn_for_dato(pivot_df, dato_mm_dd):
    if dato_mm_dd not in pivot_df.index:
        print(f"Ingen data funnet for {dato_mm_dd}")
        return
    pivot_df.loc[dato_mm_dd].plot(kind='bar', title=f"Solskinn på {dato_mm_dd}")
    plt.ylabel("Solskinnstimer")
    plt.tight_layout()
    plt.show()

# ---------- STEG 4: Månedlig aggregering ----------
def aggreger_til_måneder(df):
    df['month_name'] = df['date'].dt.strftime('%B')
    df['year'] = df['date'].dt.year
    pivot = df.groupby(['year', 'month_name'])['sunshine_hours'].sum().reset_index()
    pivot_df = pivot.pivot(index='month_name', columns='year', values='sunshine_hours')
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    pivot_df = pivot_df.reindex(months_order)
    
    pivot_df.plot(kind='bar', figsize=(12, 6), title="Månedlig solskinn per år")
    plt.ylabel("Solskinnstimer")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------- Kjør alt ----------
if __name__ == "__main__":
    df = forbered_og_last_data()
    daglig_pivot = lag_daglig_graf(df)

    # Valgfritt: Spør bruker om spesifikk dato
    dato_input = input("\nSkriv inn en dato (mm-dd) for å se solskinn den dagen over flere år (eller Enter for å hoppe over): ")
    if dato_input:
        vis_solskinn_for_dato(daglig_pivot, dato_input)

    # Valgfritt: Vis månedlig aggregering
    vis_mnd = input("\nVil du se månedlig solskinn per år? (ja/nei): ")
    if vis_mnd.lower() == "ja":
        aggreger_til_måneder(df)
