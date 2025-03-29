import os
import requests
import pandas as pd

#slik at csv filen skal lagres i rikig mappe (data)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

from variabler import client_id, stasjon_id, elementer, tidsperioder

def hent_solskinnstimer(element, periode, filnavn):
    
    endpoint = "https://frost.met.no/observations/v0.jsonld"
    params = {
        "sources": stasjon_id,
        "elements": elementer[element],
        "referencetime": tidsperioder[periode]
    }
    
    response = requests.get(endpoint, params=params, auth=(client_id, ""))
    
    if response.status_code == 200:
        data = response.json()
        lagreCSV(data, filnavn)  
        return data
    else:
        print(f"Feil {response.status_code}: {response.text}")
        return None
    
def lagreCSV(data, filnavn):

    lagret = []
    for item in data.get("data", []):
        lagret.append({
            "date": item["referenceTime"],
            "sunshine_hours": item["observations"][0]["value"]
        })

    if lagret:  # Hvis det er data tilgjengelig
        # Lagre dataene i en pandas DataFrame
        df = pd.DataFrame(lagret)
        
        # Bygg filbanen til 'data' mappen
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', filnavn)
        
        # Sørg for at mappen eksisterer, hvis ikke, lag den
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Lagre DataFrame som en CSV-fil
        df.to_csv(filename, index=False)
        print(f" Rådata lagret: {filename}")
    else:
        print(" Ingen data tilgjengelig for lagring.")

'''   
for å opprette data med terminal
if __name__ == "__main__":
    hent_solskinnstimer("t_månder", "seksten", "raa_data_m")

if __name__ == "__main__":
    hent_solskinnstimer("t_dager", "tjue", "raa_data_d")
    
''' 