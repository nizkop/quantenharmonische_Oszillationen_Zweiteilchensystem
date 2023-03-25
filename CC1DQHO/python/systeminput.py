from math import * 

def ar(a, e, s):
	global xDist
	global zDist
	for i in range(int(10*a),int(10*e),int(10*s)):
            xDist += [i/10]
            zDist += [i/10]
	return 

f = open("systems.inp", "w")
f.write("mass\tfConst\trSep\txDist\t\t\tzDist\n")

mass = 1.0
fConst = 0.1
rSep = 2.0

xDist = []
zDist = []
ar(0, 2, 0.1)
ar(2, 10, 0.5)
ar(10, 60, 1) 

for x in xDist:
	for z in zDist:
            if x == 0 or z == 0:# or x == z: 
                f.write( str(mass) + "\t" +str( fConst) + "\t" + 
			str(rSep) + "\t" + 
			str(x) + "\t\t\t" + str(z) + "\n" )
            elif x == z:
                f.write( str(mass) + "\t" +str( fConst) + "\t" +
                        str(rSep) + "\t" +
                        str(  x / sqrt(2) )   + "\t" 
                         + str( z / sqrt(2) ) + "\n" )


f.close()
