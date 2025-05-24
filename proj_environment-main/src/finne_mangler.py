import pandas as pd

def finne_hull(filbane,dato_kolonne):
    # først lese inn data
    df = pd.read_csv(filbane)

    #konverterer til datetime slik at pandas bahandler datoene som datoer og ikke vanlig tekst
    df[dato_kolonne] = pd.to_datetime(df[dato_kolonne])
    

    #sorterer datoene
    df = df.sort_values(by=dato_kolonne).reset_index(drop=True)

    #leter etter duplikat
    duplikater = df[df.duplicated()]

    #lage en liste med datoer som kan brukes til sammenligning for å finne differanser
    full_dato_range = pd.date_range(start=df[dato_kolonne].min(),
                                    end=df[dato_kolonne].max(),
                                    freq='D')
    
    #finne datoene som mangler
    manglende_datoer = full_dato_range.difference(df[dato_kolonne])

    #printer ut funnene
    print("antall totale rader i datasettet:", len(df))
    print("antall dupliserte datoer:", len(duplikater))
    print("antall datoer som mangler:", len(manglende_datoer))

    if not duplikater.empty:
        print("\nDupliserte datoer:")
        print(duplikater[dato_kolonne])

    if len(manglende_datoer) > 0:
        print("\nManglende datoer:")
        print([dato.strftime("%Y-%m-%d") for dato in manglende_datoer])

    return duplikater, manglende_datoer


def vasket_data(filbane, dato_kolonne, output_fil="utfylt_data.csv"):
    # _, gjør at vi ikke henter første return verdi fra finne_hull funksjonen
    _, manglende_datoer = finne_hull(filbane, dato_kolonne)

    #lese inn rå data filen
    df = pd.read_csv(filbane)
    df[dato_kolonne] = pd.to_datetime(df[dato_kolonne])
    df = df.sort_values(by=dato_kolonne).reset_index(drop=True)

    #fjerner duplikater
    df = df.drop_duplicates()

    #putter de manglende datoene inni et dataframe
    df_manglende = pd.DataFrame({dato_kolonne: manglende_datoer})

    #om det skulle være noen kolonner med verdi NaN ønsker vi også å hente disse og legge de sammen med de andre manglende verdiene
    for col in df.columns:
        if col !=dato_kolonne:
            df_manglende[col] = pd.NA

    #legger sammen de orginale og de manglende 
    df_utfylt = pd.concat([df, df_manglende], ignore_index=True)
    df_utfylt = df_utfylt.sort_values(by=dato_kolonne).reset_index(drop=True)

    #for å fylle ut bruker vi linjær interpolate, altså antar en rett linje mellom punktene
    df_utfylt.interpolate(method="linear", inplace=True)

    #lagrer filen i data mappen
    output_filbane = "../data/utfylt_data.csv"

    #lagrer oppdatert info i ny fil 
    df_utfylt.to_csv(output_filbane, index=False)
    print(f"\nBenyttet lineær interpolasjon, fil lagret som : {output_fil}")


    return df_utfylt