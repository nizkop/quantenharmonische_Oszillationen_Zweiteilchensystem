include("Grundzustandsarray.txt")
array2 = []
append!(array2, [["odist","pdist", "force", "mass", "E0"]])

for i in 1:length(array)
	j = array[i][1]
	if j == 1.0 || j == 10.0 || j == 20.0 || j == 30.0 || j == 40.0
		append!(array2, [ array[i]  ] ) 
	end
end

println(array2)



for i in 2:length(array2)
	x = 0.5 - ( array2[i][5] - 1/ array2[i][1]) 
	append!(array2[i], [x] ) 
end

println(array2) 



