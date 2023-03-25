

include("Grundzustandsarray_CC.txt")#Definition des arrays mit Abständen, Masse & Kraftkonstante, Grundzustandsenergien




append!(array[1], [ "\tTerm 2" ] )
append!(array[1], [ "\tE - Term 2" ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
        n = 0
	a = (mass*force)^(-1/2) 
	r = ( array[i][1] ^2 + array[i][2] ^2)^(1/2) 
        omega = sqrt( force/mass)
        x = ( (2* array[i][2]^2 - array[i][1]^2 ) *  a^(-3) * r^(-5/2) /2  )
        append!(array[i], [x] )
	 append!(array[i], [ array[i][7] - x     ] )
end


#println(array)


include("suche2.jl")
Arrayspeichern(array,"Grundzustandsarray_tst.txt") 
tabelle("Tabelle_tst.txt")#array muss array heißen!  


