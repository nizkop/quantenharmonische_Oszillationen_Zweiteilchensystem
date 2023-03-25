import sys
import matplotlib.pyplot as plt


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


def Dateiname(a = "", b = "out"): # Anhang " z" an Variable a für zurückübersetzen von "DLPNO"-Filename zu "RHF" 
	import sys
	global datei 
	datei = sys.argv[1] #"B4N4-RHF-ccPVTZ-OPT-conf1" #sys.argv[1]
	if "DLPNO" in a: 
		dateiname = datei[:datei.find("-")] #! finden den 1. "-"
		if a =="DLPNO z": 
			A = "-RHF-ccPVTZ-OPT"
		else: 
			A = "-DLPNO-ccPVTZ"
		
		if "conf" in datei:
			x = datei.find("conf")
			A += "-" + datei[x: x+5]
		if a =="DLPNO z":
			return dateiname + A +"-FREQ-optimiert"+ "."+b
		a = A 
	else:
		if len(a) > 0:
			a =  "-" + a
		dateiname = datei
	dateiname += a + "."+b
	return dateiname

#a = "", "start", "optimiert" , "FREQ" 
#b = "out", "xyz", "txt" , "inp" 


#print( Dateiname() ) 


def Einlesen(dateiname):
	f = open(dateiname, "r") #,encoding='cp1252'
	alles = f.readlines()
	f.close()
	return alles





def winkel(a,b,c):
        import math 
        from Koordinatenauswertung import genauigkeit
        #a = mittleres Atom
        vek1=[]
        vek2=[]
        for i in range(len(a)):
                vek1 +=[ a[i] - b[i] ]
                vek2 += [ a[i] - c[i] ]
        s = prod(vek1, vek2)
        #print("s", s)
        l1 = laenge(vek1)
        l2 = laenge(vek2) 
        #print("l2", l2, 3**0.5)
        phi = math.acos( s  / ( l1 * l2) ) # in RAD
        return round(phi*180/math.pi, genauigkeit) 


#Test:
#print( winkel( [0,0,0], [1,0,0], [0,1,0] ) )

def Max(l,): #Koordinatenauswertung.py
                m = l[0][0]
                for i in l:
                        for j in i:
                                if j > m:
                                        m = j
                return m


def Min(l): #Koordinatenauswertung.py
        m = l[0][0]
        for i in l:
                for j in i:
                        if j < m:
                                m = j
        return m


def laenge(v):
        l = 0
        for i in v:
                l += i**2
        return l**(0.5) 

import math

def prod(v1,v2):
        s = 0
        for i in range(len(v1)):
                s += v1[i] * v2[i]
        return s


''' alt = nur für Latextabellenanlegen: 
def auftrennen(string, f=""):
    if string[0] == "\n":
        return f+" \\\ "+string[0]
    elif string[0] == " " or string[0] == "\t":
        if len(f) > 0 and f[-1] != "&":
                f += "\t &" 
    else:
        f += string[0]
    return auftrennen(string[1:], f)
'''
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


def Genauigkeit(c): 
    global genauigkeit
    genauigkeit =  len(c[0][1]) -1 - c[0][1].find(".")
    return genauigkeit



def plotliste(alles): 
        liste =[[]]
        for i in range(0,len(alles)):
            if alles[i] =="\n":
                pass
            else:
                #print( [ alles[i]] ) 
                a =   auftrennen(alles[i], aus ="diag")  
                #print(a)
                for j in range(len(a)):
                    while j+1 > len(liste):
                        liste += [[]] 
                        #print(liste, len(liste)) 
                    #print("a[j]", a[j]) 
                    #print("liste[j]", type(liste[j]) ) 
                    liste[j] += [ a[j] ]
        return liste


def mol_anzahl(liste): #liste mit den Molekülnamen 
        grenze_BN = 0
        grenze_BeO = 0
        for i in range(len(liste)):
            if grenze_BN == 0:
                if "N" in liste[i]:
                    pass
                else:
                    grenze_BN = i
            elif grenze_BeO == 0:
                if "Be" in liste[i]:
                    pass
                else:
                    grenze_BeO = i
            else:
                break
        return [grenze_BN, grenze_BeO]


#Gesamtatomanzahlen raussuchen aus Molekülname:
def gesamtatomanzahl(liste):
        #sucht aus Atomnamen die Atomanzahlen heraus, addiert sie und hängt sie als Liste an das vorgegebene Array an
        l = len(liste)
        liste += [[]] 

        for i in range(len(liste[0])):
            nr = 0
            j = 0
            while j <= len(liste[0][i]):
                try:
                       try:# für Zahlen > 9  
                        nr += int( liste[0][i][j:j+2] ) 
                        j += 1
                       except: # Zahlen < 10 bzw. Ende 
                        nr += int( liste[0][i][j] ) 
                except:
                       pass
                j += 1
            liste[l] += [nr]
        # ! Index l sollte Index -1 der liste entsprechen
        return liste


#allgemeines Aufteilen der Zeilen nach Leerzeichen etc.:
def zeilenaufteilen(b): # b = Array mit Strings von Zeilen 
    c = []
    for i in b:
            e = "" #Var. für einzelne Werte /Angaben in der Zeile
            d = [] #Array der einzelnen Zeilen
            for j in i:
                    if j == " " or j == "\t" or j == "\n":
                            if len(e) >= 1:
                                    d += [e]
                            e = ""
                    else:
                            e += j
            c += [d]
    return c

def diagramm_t1(liste, grenze_BN, grenze_BeO): 
        #einzeln für BN, BeO & LiF: 
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
            xAchse ="Gesamtatomanzahl n [-]", Titel ="Energieübersicht ("+art+")")
    if a == 1 or a == 3:
        y = "[Eh]"
    elif a==2 or a == 4:
        y ="[eV]"
    plt.ylabel("Energie "+y)
    plt.legend()
    plt.savefig("Energien-"+art+".pdf", bbox_inches="tight")
    plt.close()
    return


def D(t): 
	T1 = ""
	if len(t) < 0: return
	#hinter der Zahl sind noch Leerzeichen -> Entfernen: 
	i = len(t)-1 #letzter Index
	while i>= 0 and (t[i] == " " or t[i] =="\n" or t[i] =="\t"): #! Reihenfolge der Bedingungen soherum, da sonst Indexerror
		i -= 1
	#print(len(t)-i) # = Anzahl Leerzeichen etc. hinten 
	for i in range(i, -1 , -1): 
			if t[i] in zahlen or t[i] ==".":
				T1 = t[i] + T1 
			else: 
				return T1


####################################################




atome = ["C", "B", "N" ,"Be", "O", "Li", "F"]
zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]




