
array = [["odist"], ["pdist"], ["k"],["E0"]]


function f(odist, pdist, k=1, mass=1) 
	append!( array[1], [string(odist)])
        append!( array[2], [string(pdist)])
	append!( array[3], [string(k)])
	filename = "energies_pdist" * string(pdist)*"_odist"* string(odist)*".dat"
	open(filename, "r") do io
		zeile = readline(io)
		append!( array[4], [zeile[4:end]])
	end
end


odist = 0.0
for pdist in 1:0.1:15
	try
	f(odist, pdist)
	catch
	end
end

pdist = 0.0
for odist in 1:0.1:15
	try
		f(odist,pdist)
	catch
	end
end


#print(array)

println(length(array[1]))
println(length(array[2]))
println(length(array[3]))




open("ubersicht_grund.txt","w") do io
	for i in 1:length(array[1])
		try
			energy = array[3][i]
		catch
			energy = "X"
		end 
		#	odist = "-"
		println(array[1][i] , "\t", array[2][i] , "\t", energy) 
	end
end



