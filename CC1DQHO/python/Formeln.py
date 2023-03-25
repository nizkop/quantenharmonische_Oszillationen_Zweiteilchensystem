import sys
import matplotlib.pyplot as plt
from math import * 

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


def Einlesen(dateiname):
	f = open(dateiname, "r") #,encoding='cp1252'
	alles = f.readlines()
	f.close()
	return alles

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




zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-"] 



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



def bez(a):
	if a == 1:	return "Z = 0" #"entlang x"
	if a == 0:	return "X = 0" #"entlang z"
	if a == 2:	return "X = Z" #"diagonal"
	else:		return "Rest" 

def Max_index(l):
	b = max(l) 
	for a in range(len(l)):
		if l[a] == b: return a
	return print("kein Maximalwert in der Liste") 





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

