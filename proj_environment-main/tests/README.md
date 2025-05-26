# Unittests

Målet med unittestene er å sjekke om funksjonene som er lagt fungerer som de skal, for å teste dette har vi lagd tester som importerer funksjonene og testet dem. Testene er skrevet i Arrange-Act-Assert, for at strukturen skal være enkel å lese, gjør den enkel å vedlikeholde, klare separasjoner og ungår rot. 

**Testmappen inneholder**
|Navn                      |Tester til mappen           |
|--------------------------|----------------------------|
|test_csv.py               |tester til hente_apidata.py |
|test_inj_reg.py           |tester til linjaer_reg.py   |
|test_linjediagram.py      |tester til linjediagram.py  |
|test_mangel_duplikat.py   |tester til finne_mangel.py  |
|test_statistikk.py        |tester til sentralmal.py    |

### Hvordan kjøre testene
For å kjøre testen man ønsker trenger man å skrive inn: python -m unittest tests.fillen_som_skal_testes
For testfilen man øsnker å teste, fyller man det inn hvor det står 'filen_som_skal_testes', og tests refererer til mappen tests som testene ligger i.

### Testene
Testene som er brukt er i stor grad positive tester som tester om funksjonen fungerer som forventet, det er lagt inn en negativ test i test_mangel_duplikat.py som tester om funksjonen finner feiltilstander i dataene.

