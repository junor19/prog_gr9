Explains the source code structure

hent_solskinnstimer(element, periode, filnavn) 
    henter solskinnsdata fra MET Norway API
    Args:
        elementer (str): "t_månder" (timer med sol per månede) eller "t_dager" (timer med sol per døgn)
        tidsperioder (str): "seksten"(2016-2020) eller "tjue"(2020-2021)
    
    Returns:
        JSON-data fra MET API eller None hvis feil.

lagreCSV(data, filnavn) 
    lagrer API-dataen i en CSV-fil


if __name__ == "__main__"
    for å opprette data med terminal