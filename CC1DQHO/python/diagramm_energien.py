
from Formeln import * 
alles = Einlesen("energien.txt") # je Zeile ein Arrayeintrag

liste = plotliste(alles[3:]) # richtig strukturiertes Array für Diagramm später 

# Zahlen umwandeln:
liste = Durchgehen(liste)
# Spalte 0: Molekülbezeichnung 
# Spalte 1: DLPNO-CCSD(T) in Eh
# Spalte 2: DLPNO-CCSD(T) in eV
# Spalte 3: RHF in Eh
# Spalte 4: RHF in eV 


#Unterteilen der x-Koordinate:
a = mol_anzahl(liste[0])
grenze_BN = a[0]
grenze_BeO = a[1]


#Gesamtatomanzahlen raussuchen aus Molekülname:
liste = gesamtatomanzahl(liste)  



#Diagramm:  (hier für Energien) 
#! Auswahl der Energiespalte (CC vs. RHF, Eh vs. eV) 

diagramm_en(liste, grenze_BN, grenze_BeO, art="CC,Eh") 
diagramm_en(liste, grenze_BN, grenze_BeO, art="CC,eV")
diagramm_en(liste, grenze_BN, grenze_BeO, art="RHF,Eh")
diagramm_en(liste, grenze_BN, grenze_BeO, art="RHF,eV")









