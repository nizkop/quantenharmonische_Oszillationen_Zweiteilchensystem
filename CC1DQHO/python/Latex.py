#Umwandlung von xyz-File in Latextabelle:

from Formeln import *

typ = ""
try:
    dateiname = Dateiname(b = "")
    alles=Einlesen(dateiname)
    typ = "xyz"
    alles = alles[2:]
except:
    import sys
    dateiname = sys.argv[1]
    alles = Einlesen(dateiname) 
    typ = "alles"


if "kurz" in dateiname:  # = Tabelle, aus der die Spalten gleicher Werte gekürzt wurden -> Extrazeilen oben für Angabe dieser gl. Werte 
    titel = alles[0][1:-1] # titel: "#" vor mass muss entfernt werden, \n am Ende abgeschnitten
    alles = zeilenaufteilen(alles)
    a = alles[2] # Tabellenkopf 
    daten = Durchgehen(alles[3:] ) 
else:
    titel = dateiname
    alles = zeilenaufteilen(alles)
    a = alles[0]
    a[0] = a[0][1:] # Entfernen #   
    daten = Durchgehen(alles[1:] ) 



# Formelzeichen, Schreibweise:
nachkomma = 3 #4 führende Stellen
e = "aus" #Ein-/Ausschalten der 10er-Schreibweise
nuller = "aus" #verändern (!= "aus"), wenn keine 10^{+00} geschreiben werden sollen
art ="e" #f für runden auf (nachkomma) Stellen, e für Exp.formatanzeige mit (nachkomma) Kommastellen
for i in range(len(daten)): # schon vorher ins passende Zahlenformat gebracht (gerundet etc.) 
    for j in range(len(daten[i])):
        daten[i][j] = "$" + str(( daten[i][j])) + "$" #Formel für Zahlen


       

#für Tabellenfangang: 
zeile1 = "\hline\n"
for i in range(len(a)):
        zeile1 += a[i] + " " 
        if i < len(daten[-1])-1:
            zeile1 += "\t &"
zeile1 += "\\\ \hline \n"


#Spaltenbreite: 
breite = (21-6) / len(daten[-1] )  
breite = str(breite) + "cm"



#Dateianlegen: 
if "xyz"in dateiname:
    dateiname = Dateiname("tabelle", "txt")
else:
    dateiname += "-Latex"



f = open( dateiname, "w")
#Tabellenkopf: 
f.write( "\\begin{table}[H] \n \caption{" + titel + "} \n \label{} \n \\begin{tabular}{") 
for i in range(len(daten[-1])):
    f.write( "p{" + breite + "}" )
f.write( "}\n" ) 
#Kopfzeile der Tabelle: Erläuterungen der Werte: 
f.write(zeile1)
#Werte in der Tabelle:
for i in daten:
        if len(i) > 0: # daten kann mal Leerelement enthalten (durch Leerzeile im Input)
            for j in range(0,len(i) -1):
                f.write( str( i[j] ) + "\t & ")
            f.write( str(i[-1])+ " " )
            l = len(daten[-1])  - len(i)
            #print(i,j, l)
            f.write("\t &"*l)  # Ergänzen leerer Spalten bis zur max. Spaltenanzahl (ggf. 0-mal, wenn bereits vollständig)
            f.write("  \\\ \n")
#Tabellenabschluss: 
f.write( " \hline \n \\end{tabular} \end{table} \n ")
f.close()





