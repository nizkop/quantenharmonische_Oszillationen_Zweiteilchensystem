#Auswertung:

include("funktionen_auswertung.jl")



#Heraussuchen der Daten, Schreiben in Array
array = grundzustandsarray()
#print(grundzustandsarray())
Arrayspeichern(array, "Grundzustandsarray.txt")  #Definition des arrays mit Abständen, Masse & Kraftkonstante, Grundzustandsenergien
tabelle("uebersicht_grund.txt")#Übersicht der Parameter der Rechnungen 

array_grund = array #Kopie des zugrundeliegenden Arrays mit reinen Parametern 



#Energiebeiträge anhängen an Array 

#Oszillation
anhaengen("E(osz) ", f_osz )

# Ladungsabstoßung / Coulomb
anhaengen("E(CC)  ", f_CC)

#Ladung-Quadrupol-Term:
anhaengen("E(Lad.-Quadr.) ", f_CQ)

#Quadrupol-Term:
anhaengen("E(QQ)", f_QQ )

#R4-Term:
anhaengen("E(D)", f_D )

#Speichern der Energiebeiträge als Array & Tabelle: 
Arrayspeichern(array,"Array_Energiebeiträge.txt")
tabelle("Tabelle_Energiebeiträge.txt")#array muss array heißen!

array_beitraege = array #Kopie des Energiebeitragsarrays 

array = array_grund #Array erneut als reine Parameterversion (Anhängen anderer/neuer Terme)


## Berechnen der Energiedifferenzen (E0 - Energiebeiträge)
	#! Bezug auf letzte Energiedifferenz im Array = fortsetzende Berechnung
anhaengen("E0_E(osz)", f_osz , true)
anhaengen("& -E(CC)" , f_CC,  true)
anhaengen("& -E(CQ)", f_CQ ,  true)
anhaengen("& -E(QQ)", f_QQ ,  true)
anhaengen("& -E(D)", f_D , true) 


Arrayspeichern(array,"Array_differenzen.txt")
tabelle("Tabelle_Differenzen.txt")

array_energiedifferenzen = array #Kopie des Arrays mit den Energiedifferenzen








