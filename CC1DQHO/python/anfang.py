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




def z(l):  # Suchen der Indizes der veränderten Werte in Array mit Unterarrays 
    a = len(l) 
    if a == 0: return
    b = len(l[0])
    v = [] # Array für geänderte Werte
    for k in range(b):
        x = l[0][k]
        for j in range(1,a):
            if l[j][k] != x:
                v += [k] 
                break 
    return v


def raus_kurz(l,dateiname):
    global liste
    if len(l) <= 1: # = keine Werte, 1 -> nciht vergleichbar 
            return
    ver = z(l)
    f = open(dateiname+"-kurz.txt", "w")
    #Schreiben der unveränderten Werte als Überschrift 
    for k in range(len(l[0])):
        if k not in ver:
            f.write( str( liste[0][k]) + " "+ str( l[0][k] ) + ", ") 
    f.write("\n\n")
    #Tabellekopf:
    for k in range(len(liste[0]) ) : 
        if k in ver: 
            f.write( str(liste[0][k] )+ "\t" ) 
    f.write("\n") 
    #Werte: 
    for k in l:
        for j in range(len(k)) :
            if j in z(l): 
                f.write(str(k[j] ) + "\t")
        f.write("\n")
    f.close()
    return




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


def abstand(x, z):
        return round( ( x*x + z*z)**(1/2) , 2)   

def Abstand(a):
        global L
        if len(L[a]) == 0: #Verschiebungen, die nicht entlang der Achse geschehen 
                return
        liste[0] = liste[0][:5] + ["abstand"] + liste[0][5:] 
        for b in range(len(L[a])):
                x = L[a][b][3] #xDist
                z = L[a][b][4] #zDist
                L[a][b] = L[a][b][:5] + [abstand(x,z)] + L[a][b][5:]















#################################################################################

import matplotlib.pyplot as plt
import sys
genauigkeit = 6
try:
    tech = sys.argv[1] 
except:
    tech =  "nein" #Auswertung der tech. Variation


try:
    datei = sys.argv[2] 
except:
    datei = "eigenvalues.tab"




###################################
liste = Einlesen(datei) # je Zeile ein Arrayeintrag

for a in range(len(liste)):
    liste[a] =auftrennen(liste[a] , aus ="diag") 



#Heraussuchen des Spaltenindex I der Grundzustandsenergien: 
for i in range(len(liste[0])):
    if liste[0][i] == 'eigenvalues':
        break



#testen auf nicht veraenderte Werte:
'''
ver = [] # Array der Indizes der veraenderten Spaltenwerte (ausser der Energien)
gleich = aenderung(0) 
for a in range(1,i):
    ver += aenderung(a)
if len(gleich) > 0: 
    gleich=gleich[:-1] #Entfernen "_" am Ende  

print("gleich:", gleich, "Indizes der gleichen Werte", ver) 
'''


ver = z(liste[1:])
print("Indizes der veränderten Werte:")
for a in ver:
        if a <= i:
                print("   - Spalten: ", a, " = ", liste[0][a] )


#ggf. enthaltene Zahlen umwandeln:
liste = Durchgehen(liste)



#Vergleich gleicher Systemparameter, veraenderter techn. Parameter -> Energien sollten gleich sein:
#Sortierspaltenindizes:
if tech =="ja":
        s1 = 3 #xDist
        s2 = 4 #zDist
else: # tech =="exakt":
        s1 = 5 #nbFcts
        s2 = 6 # nbGHpoints

        
#sortieren: 
l = sorted(liste[1:], key=lambda a_entry: a_entry[s1])
l = sorted(l, key=lambda a_entry: a_entry[s2])


if tech== "nein": #Herauskürzen der Energien angeregter Zustände 
        for a in range(len(l)):
                l[a] = l[a][:i+1]


f = open("umsortiert.txt", "w")
for a in liste[0]:
    f.write(str(a) + "\t" )
f.write("\n")
for a in range(len(l)):
    for b in range(len(l[a])):
        if len(str(l[a][b])) > 6:
            try:
                c = "%0."+str(genauigkeit)+ "f" # muss zweizeilig aufgeteilt sein
                l[a][b] = c % round(l[a][b], genauigkeit) 
            except: 
                pass
        f.write(str(l[a][b])  + "\t")
    f.write("\n"  ) 
f.close() 



if tech != "ja":
        L = [ [], [], [] , [] ] #3 = für Variation entlang x, z & diagonal
        
        for a in range(len(l)):
                if l[a][3] == 0.0: #Finden xDist = 0
                        L[0] += [l[a]]
                if l[a][4] == 0.0:
                        L[1] += [l[a]]
                if l[a][3] == l[a][4]:
                        L[2] += [l[a]]
                if l[a][3] != 0.0 and l[a][4] != 0.0 and l[a][3] != l[a][4]:
                        L[3] += [l[a]]             

           
#Abstände einschieben für Diagonalwerte etc.:
if tech != "ja":
        for a in range(2,4):
             Abstand(a) 
        for a in range(len(L)) : #ueber Anzahl variierter techn. Parameter-Saetze 
            raus_kurz(L[a], "sysPar-"+str(a) )  


raus_kurz(l, dateiname = "uebersicht")


#Diagramm für Systemvariation:
if tech != "ja":
        for a in range(len(L)):
                if len(L[a]) <= 2:      break
                if a == 0:
                        label = "entlang x"
                        ix = 4 #Index für zDist, da z variiert
                        iy = i
                elif a == 1:
                        label = "entlang z"
                        ix = 3 # x variiert 
                        iy = i
                elif a == 2:
                        label = "diagonal"
                        ix = 5 #eingeschobene Abstände
                        iy = i+1
                else:
                        label = "Rest" 
                        ix = 5 
                        iy = i+1
                #print( "L[a]", L[a] )
                #print("ix", ix, " iy",iy, " i", i) 
                x = []
                y = []
                for b in range(len(L[a])) :
                    x += [ float( L[a][b][ix] )]
                    y += [float(L[a][b][iy])]
                #print( "x", x, "\n", "y", y ) 
                Diagramm(x = x , y = y, Label= label, style = "x" ,
                         xAchse = "Abstand", yAchse= "Energie [Eh]" , 
                         Titel = "sysPar: Übersicht Energiverhalten mit Abstandsvariation") 
        plt.legend()
        plt.savefig("abstaende.pdf") 
        plt.close()
        



#Auftrennung für Variation techn. Parameter: 
#Liste fuer die Systeme gleicher Entfernung:
if tech == "ja":  
        L = [[  l[0] ]]  
        M = l[0][:5]   #Array-Variable fuers Merken der aktuellen Systemparameter 

        for a in range(1,len(l)):
            if l[a][:5] == M:#inkl. Spalte 5 (= Index 4)
                L[-1] += [ l[a] ] 
            else:
                L += [[ l[a] ]] 
                M = l[a][:5] 
        

        for a in range(len(L)) : #ueber Anzahl variierter techn.Parameter-Saetze 
            raus_kurz(L[a], "techPar-"+str(a) ) 





 
