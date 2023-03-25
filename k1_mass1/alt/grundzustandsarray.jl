#Erstellen eines Array mit den Abständen und Energien für den Grundzustand:

function grundzustandsarray()

	array = [["odist"], ["pdist"], ["k"],["mass"], ["E0          "]]


	function f(odist, pdist, k=1, mass=1)
        	filename = "./energies/energies_pdist" * string(pdist)*"_odist"* string(odist)*".dat"
	        open(filename, "r") do io
			append!( array[1], [string(odist)])#innerhalb des files, da sonst der Fehler nicht vorhandener Datei zu spät = schon odist etc. als Werte im Array eingetragen -> ungleiche Länge der Teilarrays
                	append!( array[2], [string(pdist)])
                	append!( array[3], [string(k)])
			append!( array[4], [string(mass)] )
        	        zeile = readline(io)
                	append!( array[5], [ zeile[4:end]] ) 
	        end
	end


	odist = 0.0
	for pdist in 0:0.005:100
	       #try
	        f(odist, pdist)
	       #catch
	       #end
	end

	pdist = 0.0
	for odist in 0:0.005:100
	       try
        	        f(odist,pdist)
	       catch
	       end
	end


	#print(array)

	#println(length(array[1]))
	#println(length(array[2]))
	#println(length(array[3]))

	return array
end



#print(grundzustandsarray())
