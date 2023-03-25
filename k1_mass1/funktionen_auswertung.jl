#Funktionen zur Auswertung: 


#Erstellen eines Array mit
	#- Abständen (odist, pdist)
	#- Kraftkonstante (k) & Masse (mass) 
	# - und Energien des Grundzustands

function abschneiden(str)
        for i in 1:length(str)
        if string(str[i]) == " "  #i sonst = Char
                return str[i+2:end]
        end
        end
end


function grundzustandsarray()
        array = []#damit Datentyp nicht festgeschrieben
        append!( array ,[ ["odist", "pdist", "force", "mass", "E0          "]])


        function f(odist, pdist, k=1, mass=1)
                filename = "./energies/energies_pdist" * string(pdist)*"_odist"* string(odist)*".dat"
                open(filename, "r") do io
                        zeile = readline(io)
                        #append!( array, [ [string(odist), string(pdist),  string(k), string(mass), zeile[4:end]]] )
                        append!( array, [ [odist,pdist,  k, mass, parse(Float64, abschneiden(zeile) ) ]] )
                end
        end


        odist = 0.0
        for pdist in 0:0.005:100
               try
                f(odist, pdist)
               catch
               end
        end

        pdist = 0.0
        for odist in 0:0.005:100
               try
                        f(odist,pdist)
               catch
               end
        end

        return array
end







#Speichern des Arrays

function Arrayspeichern(array, datei = "Grundzustandsarray.txt")
open(datei, "w") do io
        write(io, "array = ")
        write(io, string(array))
end
end


#Tabelle:
function tabelle(arraydatei)
open(arraydatei,"w") do io
        #write(io, zeile)
        for i in 1:length(array)
                for j in 1:length(array[i])
                write(io, string(array[i][j]))
                #für Abstände der Spalten: 
		n=1
		x = length(string(array[i][j]))
                #if x < 14
                #       n = 19 - 5 -  x
                #end
                # write(io, " "^n  *"\t")
                if x ==1
                        n = 4
                elseif x >= 2  &&  x  <= 7
                        n = 3
                elseif x >= 8  && x  <= 15
                        n = 2
                elseif x >= 16
                        n = 1
                end
                write(io, "\t"^n )
        end
        write(io, "\n")
        end
end
end


#Fortsetzen des Arrays durch Berechnen von Energien nach best. Funktionen f:
function anhaengen(name,f , e= false )
append!(array[1], [ "\t"*name ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
        a = (force * mass)^(-1/4)
        pdist = array[i][2]
        odist = array[i][1]
        omega = sqrt( force/mass)
	if e
		E = array[i][length(array[i])]
		x = E - f(a, odist, pdist, mass)
        else
		x =   f(a, odist, pdist, mass)
	end
        append!(array[i], [x] )
end
end

#Funktionen zur Berechnung der Energiebeiträge müssen zum Einsatz in anhangen() abhängen con a, odist, pdist, mass
#Oszillation:
function f_osz(a, odist, pdist, mass)
n= 0
return (n+1/2) /( mass*a^2)
end

# Ladungsabstoßung / Coulomb:
function f_CC(a, odist, pdist, mass)
1/ sqrt( odist^2 + pdist^2)
end

#Ladung-Quadrupol-Term:
function f_CQ(a, odist, pdist, mass)
a^2*( pdist^2 - odist^2 /2) / ((sqrt( odist^2 + pdist^2))^5  ) #odist = Z, pdist = X
end

#Quadrupol-Term:
function f_QQ(a, odist, pdist, mass)
3*a^4 * ( 8*pdist^4 - 24*pdist^2*odist^2+3*odist^4)/ ( 4 * (sqrt( odist^2 + pdist^2))^9 )
end

#R4-Term:
function f_D(a, odist, pdist, mass)
- pdist^2 * a^2 /( (1/(mass * a^4))^(1/2) * (sqrt( odist^2 + pdist^2))^5 )
end







