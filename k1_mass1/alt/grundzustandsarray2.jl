#Erstellen eines Array mit den Abständen und Energien für den Grundzustand:

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



#print(grundzustandsarray())
