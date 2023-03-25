

include("Grundzustandsarray.txt")#Definition des arrays mit Abständen, Masse & Kraftkonstante, Grundzustandsenergien



append!(array[1], [ "\t\tE(osz)" ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
        n = 0
        omega = sqrt( force/mass)
        x = (0.5+n)*omega 
	append!(array[i], [x] )
end



append!(array[1], [ "\t\tE(CC)" ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
        n = 0
        omega = sqrt( force/mass)
        x = ( 1/ sqrt( array[i][1]^2 + array[i][2]^2  ) )
        append!(array[i], [x] )
end


append!(array[1], [ "\t\tTerm 2" ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
        n = 0
        a = (mass*force)^(-1/2)
        r = ( array[i][1] ^2 + array[i][2] ^2)^(1/2)
        omega = sqrt( force/mass)
        x = ( (2* array[i][2]^2 - array[i][1]^2 ) *  a^(-3) * r^(-5/2) /2  )
        append!(array[i], [x] )
        # append!(array[i], [ array[i][7] - x     ] )
end






include("suche2.jl")
#Arrayspeichern(array,"array_tst.txt") 
tabelle("Tab_tst.txt")#array muss array heißen!  


