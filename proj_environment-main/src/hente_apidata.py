import os
import requests
import pandas as pd

from variabler import client_id, stasjon_id, elementer, tidsperioder

def hent_solskinnstimer(element, periode, filnavn):
    #viser til frost api som endpoint og deffinerer parametere som skal sendes
    endpoint = "https://frost.met.no/observations/v0.jsonld"
    params = {
        "sources": stasjon_id,
        "elements": elementer[element],
        "referencetime": tidsperioder[periode]
    }
    
    #sender forespørsel til api viktig å ha lagt in client_id i .env filen!
    response = requests.get(endpoint, params=params, auth=(client_id, ""))
    
    #om forespørselen lykkes vil dataen lagret som JSON
    if response.status_code == 200:
        data = response.json()
        lagreCSV(data, filnavn)  
        return data
    else: #om forespørselen ikke lykkes viser feilkode 
        print(f"Feil {response.status_code}: {response.text}")
        return None
    
def lagreCSV(data, filnavn):

    lagret = []

    #trekker ut spesifikt tidspunktet og solskinnstimer
    for item in data.get("data", []):
        lagret.append({
            "date": item["referenceTime"],
            "sunshine_hours": item["observations"][0]["value"]
        })



    #passer på at det faktisk finnes data før viprøver å lagre
    if lagret:  
        df = pd.DataFrame(lagret)
        
        #lager filsti slik at filen blir lagret i mappen data
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', filnavn)

        #oppretter mappen om den ikke finnes
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        #skriver dataframe til csv-fil
        df.to_csv(filename, index=False)
        print(f" Rådata lagret: {filename}")
    else:
        print(" Ingen data tilgjengelig for lagring.")


'''
Meterorologisk Institutt (n.d) frost.met.no.
    https://frost.met.no/howto.html
    https://frost.met.no/python_example.html
    https://frost.met.no/api.html

OpenAI. (n.d.). *ChatGPT (GPT-4)* [Stor språkmodell]. https://chat.openai.com/

Pandas (n.d.) pandas.pydata.org.
    https://pandas.pydata.org/docs/user_guide/index.html
    https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe

Rouhani, M. (2019). *Applied Programming — Applied Programming.* Ntnu.no. https://rouhani.folk.ntnu.no/textbooks/tdt4114/intro.html

W3Schools. (n.d.-a).  Www.w3schools.com.
    https://www.w3schools.com/python/pandas/default.asp
    https://www.w3schools.com/python/pandas/pandas_dataframes.asp
    https://www.w3schools.com/python/module_requests.asp
'''