
def Abstand(a):
        global L
        if len(L[a]) == 0: #Verschiebungen, die nicht entlang der Achse geschehen 
                return
        liste[0] = liste[0][:5] + ["abstand"] + liste[0][5:] 
        for b in range(len(L[a])):
                x = float(L[a][b][3]) #xDist
                z = float(L[a][b][4]) #zDist
                L[a][b] = L[a][b][:5] + [abstand(x,z)] + L[a][b][5:]


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
    #Tabellenkopf:
    for k in range(len(liste[0]) ) : 
        if k in ver: 
            f.write( str(liste[0][k] )+ "\t" ) 
    f.write("\n") 
    #Werte: 
    for k in l:
        for j in range(len(k)) :
            if j in z(l): 
                #print( k[j] ) 
                if j < i: 
                    ab = round( float( k[j])  , 1 ) 
                else: # Energiewerte
                    ab = k[j] 
                f.write(str( ab ) + "\t")
        f.write("\n")
    f.close()
    return


#################################################################################
#Einstellungen / Vorgaben: 

from Formeln import * 

genauigkeit = 6
try:
    tech = sys.argv[1]
except:
    tech =  "nein" #Auswertung der tech. Variation

try:
    r = sys.argv[2] 
except:
    r = "ges" # Auswahl für Diagrammbereich bei Systemvariation: "nah", "mitte", "fern"



#################################################################################
liste = Einlesen("eigenvalues.tab") # je Zeile ein Arrayeintrag

for a in range(len(liste)):
    liste[a] =auftrennen(liste[a] , aus ="diag") 



#Heraussuchen des Spaltenindex I der Grundzustandsenergien: 
for i in range(len(liste[0])):
    if liste[0][i] == 'eigenvalues':
        break



#testen auf nicht veraenderte Werte:
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
                if b >= i: 
                    c = "%0."+str(genauigkeit)+ "f" # Energienrunden
                else:
                    c = "%0."+str(2)+ "f" # für x & z (Diagonalwerte)
                l[a][b] = c % round(l[a][b], genauigkeit) # muss zweizeilig aufgeteilt sein
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





#Auftrennung für Variation techn. Parameter: 
#Liste fuer die Systeme gleicher Entfernung:
if tech == "ja":  
        L = [[  l[0] ]]  
        M = l[0][:5]   #Array-Variable fuers Merken der aktuellen Systemparameter 

        for a in range(1,len(l)):
            if l[a][:5] == M: #inkl. Spalte 5 (= Index 4)
                L[-1] += [ l[a] ] 
            else:
                L += [[ l[a] ]] 
                M = l[a][:5] 
        

        for a in range(len(L)) : #ueber Anzahl variierter techn.Parameter-Saetze 
            raus_kurz(L[a], "techPar-"+str(a) ) 


#Diagramm für Systemvariation:

if tech != "ja":
        U =  [ [], [], [] , [] ]  #für Herausschreiben der Abstände (Index 0) & Energien (Index 1) 
        for a in range(len(L)):
                if len(L[a]) <= 2:      break
                if a == 0:
                        ix = 4 #Index für zDist, da z variiert
                        iy = i
                elif a == 1:
                        ix = 3 # x variiert 
                        iy = i
                elif a == 2:
                        ix = 5 #eingeschobene Abstände
                        iy = i+1
                else: 
                        ix = 5 
                        iy = i+1
                label = bez(a) 
                x = []
                y = []
                for b in range(len(L[a])) :
                    x += [ float( L[a][b][ix] )]
                    y += [ float(L[a][b][iy]) ] 
                Diagramm(x = x , y = y, Label= label, style = "x" ,
                         xAchse = "Abstand R [a.u.]", yAchse= "Grundzustandsenergie [Eh]"
                         #, Titel = "sysPar: Übersicht Energieverhalten mit Abstandsvariation"
                         )
                U[a] = [ x , y ]
        plt.legend() 
        if r == "nah":
                plt.xlim(0,2)
                plt.ylim(0.8, 1.8) 
        elif r == "mitte":
                plt.xlim(5,10)
                plt.ylim(0.59, 0.72)
        elif r == "fern": 
                plt.xlim(10,60)
                plt.ylim(0.49, 0.62)
        else:
            plt.xlim(0, 60)
        plt.savefig( "abstaende-" + r + ".pdf")
        plt.close()

                
        #print([U]) 
        #print(len(U[0]))
        #print(len(U[0][0]))



        D = [] 
        for a in range(len(U)):
                if len(U[a]) == 0:	break
                #d = []
                for b in range(a+1, len(U)): #Vgl. Rechnungen a & b 
                        if len(U[b]) != len(U[a]): 	break #falls Unterarray leer (z.B. durch keine "Rest" Abstände)
                        #print("Kombination: ", a,b) 
                        d = []
                        for c in range(len(U[a][0])): 
                                if round(U[a][0][c],1) != round(U[b][0][c],1): #Index 0 = Abstände
                                        print("! ungleicher Abstand: ", U[a][0][c] , " und ", U[b][0][c])
                                else: # Index 1 = Energien (Grundzustand) 
                                        d += [ abs( U[b][1][c] - U[a][1][c] ) ]
                
                        D += [[  bez(a)+" zu "+bez(b) , U[a][0] , d ]] #Index 2 -> Energiedifferenzen 

        #print(D)
        #print(len(D[0]), "soll = 3")
        #print(len(D[0][2]), "soll = ", len(U[0][0]) )




        for a in range(len(D)):
                print("maximaler Unterschied der Energien bei ", D[a][1][Max_index(D[a][2])] ,"a.u. von" , max( D[a][2] ) , "Eh für ", D[a][0]  )
                Diagramm( D[a][1], D[a][2], Label= D[a][0] , xAchse = "Abstand R [a.u.]", yAchse = "Energiedifferenzbeträge [Eh]" )
        plt.legend() 
        plt.xlim(0,10)
        plt.savefig("Energiedifferenzen.pdf")












 
