points = [-0.7071067811865476, 0.7071067811865476]
nbfcts = 5 

# calculate (normalized) Hermite polynomials at quadrature points:
from hermite import * 
'''
soll: 
hvalues[0] = norm_hermite_polynomials_at_x(nbfcts,points[0])
hvalues[1] = norm_hermite_polynomials_at_x(nbfcts,points[1])
''' 
hvalues = []
for i in range(len(points)):
	hvalues += [ norm_hermite_polynomials_at_x(nbfcts,points[i]) ] 

print(hvalues)
#println(typeof(hvalues)," , " , length(hvalues)," , ", length(hvalues[1]) )