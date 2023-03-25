open("energies_pdist19.8_odist0.0.dat", "r") do io
global zeile = readline(io)
end

function abschneiden(str) 
	for i in 1:length(str) 
	if string(str[i]) == " "  #i sonst = Char 
		return str[i+2:end]
	end
	end
end


println( abschneiden(zeile)  ) 
