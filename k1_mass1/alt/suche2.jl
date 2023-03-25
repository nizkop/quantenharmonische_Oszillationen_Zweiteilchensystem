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
		n=1
		#if length(string(array[i][j])) < 14 
		#	n = 19 - 5 -  length(string(array[i][j])) 
		#end
		# write(io, " "^n  *"\t")
		if length(string(array[i][j])) ==1
			n = 4
		elseif length(string(array[i][j])) >= 2  &&  length(string(array[i][j]))  <= 7
			n = 3
		elseif length(string(array[i][j])) >= 8  && length(string(array[i][j]))   <= 15
			n = 2
		elseif length(string(array[i][j])) >= 16
			n = 1
		end 
		write(io, "\t"^n ) 
	end
	write(io, "\n")
	end
end
end



#Heraussuchen der Daten, Schreiben in Array
#include("grundzustandsarray2.jl")
#array = grundzustandsarray()

#Arrayspeichern(array)
#tabelle("uebersicht_grund.txt") 


