function ar(a, e, s)
global xDist
global zDist
for i in a:s:e
append!( xDist, [i] ) 
append!(zDist, [i] )
end
end 


mass = 1.0
fConst = 1.0
rSep = 2.0
xDist = []
zDist = []

ar(0, 2, 0.1)
ar(2.5, 10, 0.5)
ar(11, 59, 1)

open("systems.inp", "w") do io
write(io, "mass\tfConst\trSep\txDist\t\t\tzDist\n")
for x in xDist
for z in zDist
if ( x == 0 || z == 0 ) 
write(io,string(mass) * "\t" * string( fConst) * "\t" *
       string(rSep) * "\t" *
       string(x) * "\t\t\t" * string(z) * "\n" )
elseif x == z 
write( io, string(mass) * "\t" * string( fConst) * "\t" *
       string(rSep) * "\t" *
       string(  x / sqrt(2) )   * "\t"
       * string( z / sqrt(2) ) * "\n" )
end 
end
end
end
