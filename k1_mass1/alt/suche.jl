#Heraussuchen der Daten, Schreiben in Array, speichern
include("grundzustandsarray2.jl")

array = grundzustandsarray()

open("Grundzustandsarray.txt", "w") do io
	write(io, "array = ")
	write(io, string(array)) 
end


#Tabelle: 

open("uebersicht_grund.txt","w") do io
	#write(io, zeile)
	for i in 1:length(array)#! Teilarray müssen gleich lang sein
		for j in 1:length(array[i])
		write(io,string(array[i][j])) 
		write(io, "\t")
	end
	write(io, "\n")
	end
end



