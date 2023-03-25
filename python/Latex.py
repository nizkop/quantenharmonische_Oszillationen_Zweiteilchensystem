#Umwandlung von xyz-File in Latextabelle:

from Formeln import *

typ = ""
try:
    dateiname = Dateiname(b="xyz")
    alles=Einlesen(dateiname)
    typ = "xyz"
    alles = alles[2:]
except:
    import sys
    dateiname = sys.argv[1]
    alles = Einlesen(dateiname) 
    typ = "alles"


daten = zeilenaufteilen(alles)
daten = Durchgehen(daten)





# Formelzeichen, Schreibweise:
nachkomma = 3 #4 führende Stellen
nuller = "aus" #verändern (!= "aus"), wenn keine 10^{+00} geschreiben werden sollen
art ="e" #f für runden auf (nachkomma) Stellen, e für Exp.formatanzeige mit (nachkomma) Kommastellen
for i in range(len(daten)):
    for j in range(len(daten[i])):
            try:
                x = "{:."+str(nachkomma)+art+"}"
                daten[i][j] = "$" + str( x.format( float( daten[i][j]))) + "$" #Formel für Zahlen
                if "e" in daten[i][j]: # Exponenten / 10^...
                    if nuller =="aus" and daten[i][j][-3:-1] == "00":
                        daten[i][j] = daten[i][j][:-5]
                    #print(daten[i][j][-3:-1])
                    else: 
                        index = daten[i][j].find("e")
                        daten[i][j] = daten[i][j][:index] + " \cdot 10^{" + daten[i][j][index+1:-1] + "} $"
            except:
                #Kontrolle auf []-Symbole: 
                k = 0
                while k < len(daten[i][j]):
                    if daten[i][j][k] == "[":
                        print("wer",daten[i][j][:k] )
                        daten[i][j] = daten[i][j][:k] + "{" + daten[i][j][k:]
                        print(daten[i][j])
                        k += 1
                    if daten[i][j][k] == "]":
                        daten[i][j] = daten[i][j][:k+1] + "}" + daten[i][j][k+1:]
                    k+=1
                
                pass




       
#Anzahl a der Spalten:
def an(z):
	a = []
	for i in range( z ):
		a += [""] 
	return a



#Leere Arrays mit Länge der Tabellenspaltenanzahl: 
try: 
	a = an( int(sys.argv[2])  ) # für individuelle (Extra-)Angabe
except: 
	m = 0
	for i in daten:
		if len(i) > m:
			m = len(i)  
	a = an(m) # oder Wert aus der Mitte mit: len( daten[len(daten)//2] ) )
einheiten = a 


#bzw. Arrays mit der Tabellenkopfzeile für Koordinatenfiles: 
if "xyz" in dateiname: 
    einheit = "[\si{\\angstrom}]"
    a = ["Atom", "$x$", "$y$", "$z$"]
    einheiten = ["", einheit, einheit, einheit]


#für Tabellenfangang: 
zeile1 = "\hline\n"
for i in range(len(a)):
        zeile1 += a[i] + " " + einheiten[i]
        if i < len(a)-1:
            zeile1 += "\t &"
zeile1 += "\\\ \hline \n"


#Spaltenbreite: 
breite = (21-6) / len(a) 
breite = str(breite) + "cm"



#Dateianlegen: 
if "xyz"in dateiname:
    dateiname = Dateiname("tabelle", "txt")
else:
    dateiname += "-Latex"




f = open( dateiname, "w")
#Tabellenkopf: 
f.write( "\\begin{table}[h] \n \caption{} \n \label{} \n \\begin{tabular}{")
for i in range(len(a)):
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
            l = m - len(i)
            #print(i,j, l)
            f.write("\t &"*l)  # Ergänzen leerer Spalten bis zur max. Spaltenanzahl (ggf. 0-mal, wenn bereits vollständig)
            f.write("  \\\ \n")
#Tabellenabschluss: 
f.write( " \hline \n \\end{tabular} \end{table} \n ")
f.close()





