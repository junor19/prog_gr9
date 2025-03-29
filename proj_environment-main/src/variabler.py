#API-nøkkel som bør ligge i et annet doc
client_id = "bd3f25c0-324e-4a26-a507-5887be8b3c9d"

#variablene
stasjon_id = "SN68173"  #stasjons-id for gløs

elementer = {
    "t_månder": "sum(duration_of_sunshine P1M)",  #hvor mange timer med sol det har vært i den måneden.
    "t_dager": "sum(duration_of_sunshine P1D)",  #hvor mange timer med sol det har vært i døgnet.
}
    
tidsperioder = {
    "seksten": "2016-01-01/2020-01-01",  #for stasjon gløshaugen var det tilgjengelig data fra og med 2016, så det er der vi starter
    "tjue": "2020-01-01/2021-01-01",  #for å få et sett ukomplett data har vi også hentet inn data fra 2020-2021 men i timer/døgnet ikke timer/månden
}