
#Tabellenbuch der Chemie, online supporting info: 
h = 6.6260755e-34
m_e = 9.1093897e-31
a_0 = 5.29177249e-11
e = 1.60217733e-19


h_quer = h /(2 * math.pi)



def E_h(wert, endeinheit="eV"):
        #wert *= e*e/a_0
        wert *= h_quer * h_quer /( m_e * a_0 * a_0 )  # in J
        if endeinheit == "J":
                return wert
        if endeinheit == "eV":
                return wert/e
        return

#print( E_h(1, "J"), E_h(1, "eV")) 



from Formeln import * 

def durchgehen(a):
        if a == "DLPNO": 
                #x = "E(TOT)" # CCSD-Energie, s. auch "E(CCSD)
                #x = "FINAL SINGLE POINT ENERGY" # =, nur etwas genauer wie 
                x = "E(CCSD(T))" 
        if a =="RHF": x = "Total Energy"
        for i in alles:
                if x in i:
                        b = i
        return b

zahlen += ["-", "."]





#zahl = float(zahl) # E in hartree
#EeV = E_h(float(zahl), "eV") 














