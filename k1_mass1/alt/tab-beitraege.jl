

include("Grundzustandsarray.txt")#Definition des arrays mit Abständen, Masse & Kraftkonstante, Grundzustandsenergien


function anhaengen(name,f )
append!(array[1], [ "\t"*name ] )
for i in 2:length(array)
        force = array[i][3]
        mass = array[i][4]
	a = (force * mass)^(-1/4)
        pdist = array[i][2]
	odist = array[i][1]
        omega = sqrt( force/mass)
        x = Float64(  f(a, odist, pdist, mass) )
	append!(array[i], [x] )
end
end



#Oszillation
function f_osz(a, odist, pdist, mass) 
n= 0
return (n+1/2) /( mass*a^2) 
end
anhaengen("E(osz) ", f_osz ) 

# Ladungsabstoßung / Coulomb
function f_CC(a, odist, pdist, mass)
1/ sqrt( odist^2 + pdist^2) 
end
anhaengen("E(CC)  ", f_CC)


#Ladung-Quadrupol-Term:
function f_CQ(a, odist, pdist, mass)
a^2*( pdist^2 - odist^2 /2) / ((sqrt( odist^2 + pdist^2))^5  ) #odist = Z, pdist = X
end
anhaengen("E(Lad.-Quadr.) ", f_CQ) 


#Quadrupol-Term:
function f_QQ(a, odist, pdist, mass)
3*a^4 * ( 8*pdist^4 - 24*pdist^2*odist^2+3*odist^4)/ ( 4 * (sqrt( odist^2 + pdist^2))^9 ) 
end
anhaengen("E(QQ)", f_QQ ) 



# Laden der Funktionen & Speichern des Arrays als Tabelle: 
include("suche2.jl")
#Arrayspeichern(array,"array_tst.txt") 
tabelle("Tab_tst.txt")#array muss array heißen!  


