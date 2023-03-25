def Einlesen(dateiname):
	f = open(dateiname, "r") #,encoding='cp1252'
	alles = f.readlines()
	f.close()
	return alles


def Diagramm(x,y,xAchse="x-Achse", yAchse="y-Achse",
		Titel="Titel", Label="label", style="-"):
        plt.xlabel(xAchse)
        plt.ylabel(yAchse)
        if Titel != "Titel":
             plt.title(Titel)
        if Label != "label":
            plt.plot(x,y,'''{f}'''.format(f=style),label=str(Label))
        else:
            plt.plot(x,y,'''{f}'''.format(f=style))
        #plt.savefig("dfjhe.pdf")
        return


def auftrennen(string, f="", aus ="Latex"):
    if len(string) == 0 or string[0] == "\n":
        if aus =="Latex":
            return f+" \\\ "+string[0]
        else:
            return [f]
    elif string[0] == " " or string[0] == "\t":
        if aus =="Latex" and len(f) > 0 and f[-1] != "&":
                f += "\t &"
        elif aus =="diag":
            if len(f) == 0: 
                return auftrennen(string[1:], f="", aus = aus )
            else:
                return [f] + auftrennen(string[1:], f="", aus = aus ) 
    else:
        f += string[0]
    return auftrennen(string[1:], f, aus)



def Durchgehen(c):
    for i in range(len(c)):
            for j in range(len(c[i])):
                    try:
                             c[i][j] = float(c[i][j])
                             # !? Nachkommastellen Float anpassen!!!
                    except:
                            pass
    return c


def diagramm_t1(liste, grenze_BN, grenze_BeO): 
        #einzeln fuer BN, BeO und LiF: 
        #print( liste[0][:grenze_BN]  )
        Diagramm(liste[-1][:grenze_BN], liste[1][:grenze_BN], Label ="BN", style = "o" ) 
        #print( liste[0][grenze_BN:grenze_BeO]  )
        Diagramm(liste[-1][grenze_BN:grenze_BeO], liste[1][grenze_BN:grenze_BeO] ,
                style ="x", Label = "BeO")
        #print( liste[0][grenze_BeO:]  )
        Diagramm(liste[-1][grenze_BeO:], liste[1][grenze_BeO:], Label ="LiF",
                Titel ="DLPNO-CCSD(T), T1 diagnostic", xAchse = "Atomanzahl n",
                yAchse ="T1-diagnostic Wert", style = "*" )

        plt.xlim()
        plt.ylim( min( liste[1]  ) - 0.001 ,  0.021)
        #plt.legend(shadow ="False" ) #lns, labs, loc ="right", bbox_to_anchor=(0.5, 1)      )
        plt.legend(framealpha=1, frameon = "True")
        
        plt.axhline(y=0.02, color='r', linestyle='-')
        plt.savefig("T1-diagnostic.pdf", bbox_inches="tight")
        plt.close()
        return


def diagramm_en(liste, grenze_BN, grenze_BeO, art):
    #Auswahl der Energiespalte (CC vs. RHF, Eh vs. eV)
    if art =="CC,Eh":
        a = 1
    elif art =="CC,eV":
        a = 2
    elif art=="RHF,Eh":
        a = 3
    elif art =="RHF,eV":
        a = 4

    Diagramm(liste[-1][:grenze_BN], liste[a][:grenze_BN], Label ="BN", style ="o")
    Diagramm(liste[-1][grenze_BN:grenze_BeO], liste[a][grenze_BN:grenze_BeO],
            style ="x", Label="BeO")
    Diagramm(liste[-1][grenze_BeO:], liste[a][grenze_BeO:], style ="*", Label ="LiF",
            xAchse ="Gesamtatomanzahl n [-]", Titel ="Energieuebersicht ("+art+")")
    if a == 1 or a == 3:
        y = "[Eh]"
    elif a==2 or a == 4:
        y ="[eV]"
    plt.ylabel("Energie "+y)
    plt.legend()
    plt.savefig("Energien-"+art+".pdf", bbox_inches="tight")
    plt.close()
    return


#################################################################################


liste = Einlesen("eigenvalues.tab") # je Zeile ein Arrayeintrag




for i in range(len(liste)):
    liste[i] =auftrennen(liste[i] , aus ="diag") 
#print(liste) 




#Heraussuchen des Spaltenindex der Grundzustandsenergien: 
for i in range(len(liste[0])):
    if liste[0][i] == 'eigenvalues':
        break
#print(i, liste[0][i] ) 


#testen auf nicht veraenderte Werte:
def aenderung(x):
   global liste 
   global ver
   vorwert = liste[1][x] #1. Datenzeile 
   for a in range(2, len(liste)):
           b = liste[a][x]
           if b != vorwert:
               ver += [a]
               return ""
   return str(liste[0][x]) + b +"_" #Generiert String, der die identischen Parameter aneinanderreiht 

ver = [] # Array der Indizes der veraenderten Spaltenwerte (ausser der Energien)
gleich = aenderung(0) 
for a in range(1,i): 
    gleich += aenderung(a)
if len(gleich) > 0: 
    gleich=gleich[:-1] #Entfernen "_" am Ende  

print("gleich:", gleich, "Indizes der gleichen Werte", ver) 



#ggf. enthaltene Zahlen umwandeln:
liste = Durchgehen(liste)



#Vergleich gleicher Systemparameter, veraenderter techn. Parameter -> Energien sollten gleich sein:

l = sorted(liste[1:], key=lambda a_entry: a_entry[3])#xDist
l = sorted(l, key=lambda a_entry: a_entry[4])#zDist

f = open("umsortiert.txt", "w")
for a in liste[0]:
    f.write(str(a) + "\t" )
f.write("\n")
for a in l:
    for b in a:
        f.write(str( b)  + "\t")
    f.write("\n"  ) 
f.close() 


#Liste fuer die Systeme gleicher Entfernung

L = [[  l[0] ]]  
M = l[0][:5]   #Array-Variable fuers Merken der aktuellen Systemparameter 

for a in range(1,len(l)):
    #print("L[-1]", L[-1] ) 
    #print( "M", M) 
    if l[a][:5] == M:#inkl. Spalte 5 (= Index 4)
        L[-1] += [ l[a] ] 
    else:
        L += [[ l[a] ]] 
        M = l[a][:5] 


#for a in L:
#    print( str(a) ) 
        




#Diagramm bzw. Übersichtsvergleich:  

import matplotlib.pyplot as plt

for a in range(len(L)) : #ueber Anzahl variierter techn.Parameter-Saetze 
    x = [0]
    for b in range(1,len(L[a]) ):
        x += [b]
    y = [ L[a][0][i] ]
    for b in range(1,len(L[a]) ) :
        y += [ L[a][b][i] ]
    #print(x, y) 
    #Titel = ""
    n ="" # str(a) 
    for c in range( len( L[a][b][:5] ) ) :
        Titel = str(liste[0][c]) + str( L[a][b][:5][c] )+ "_"
        #if c not in ver:
        n +=  str(liste[0][c]) + str( L[a][b][:5][c] )+ "_"
    #print( Titel,"\n", n) 
    Diagramm(y = y , x = x, Titel =n[:-1]  )
    plt.savefig("TecVar"+ n[:-1] +".pdf") 
    plt.close() 










