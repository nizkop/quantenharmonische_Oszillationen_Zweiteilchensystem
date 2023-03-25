

include("Grundzustandsarray.txt")#Definition des arrays mit Abständen, Masse & Kraftkonstante, Grundzustandsenergien


append!(array[1], [ "\t\tE0-E(CC)" ] ) 
for i in 2:length(array)
	force = array[i][3] 
	mass = array[i][4]
	n = 0
	omega = sqrt( force/mass)
        x = ( array[i][5] - 1/ sqrt( array[i][1]^2 + array[i][2]^2  ) ) 
        append!(array[i], [x] )
end
#



append!(array[1], [ "\tE0-E(CC)-E(osz)" ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
        n = 0
        omega = sqrt( force/mass)
        x = -(0.5+n)*omega + ( array[i][5] - 1/ sqrt( array[i][1]^2 + array[i][2]^2  ) )
        append!(array[i], [x] )
end


#println(array)


include("suche2.jl")
Arrayspeichern(array,"Grundzustandsarray_CC.txt") 
tabelle("Tabelle_CC.txt")#array muss array heißen!  


