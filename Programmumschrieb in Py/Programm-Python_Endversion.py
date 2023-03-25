#Inhalte linearer ALgebra:
import numpy as np

#Gaus-Quadratur:
import scipy 


# physical parameters:
pdist = 0.0    # parallel distance between the oscillators (in a.u.)
odist =  0.0 	# orthogonal distance between the oscillators (in a.u.)
mass =  1.0     # mass of oscillating particle (in a.u.)
force =  1.0    # force constant (in a.u.)


# technical parameters:
nbpoints = 2 # number of Gauss-Hermite integration points
nbfcts = 5   # number of QHI eigenfunctions to be used

points, weights = np.polynomial.hermite.hermgauss(nbpoints) # obtain Gauss-Hermite quadrature points and weights
# type liefert: <class 'tuple'> aus 2 Elementen der Art <class 'numpy.ndarray'>


# calculate (normalized) Hermite polynomials at quadrature points:
from hermite import * #File: hermite.py
#hvalues (original = Array{Array{Float64,1},1} ; Länge 20, Länge 1. Element = 6) 
hvalues = []
for i in range(nbpoints): # = len(points) 
		hvalues.append( norm_hermite_polynomials_at_x(nbfcts,points[i]) ) # für "import hermite" hier "hermite." vorm Funktionsaufruf

# calculate potential at quadrature points:
len = 1/sqrt(force*mass)
def pot(x):
	return 1/sqrt((odist**2)+((pdist-len*x)**2))
potval=[]
for i in range(nbpoints): # da nbpoints = len(points)
	potval += [pot(points[i])]
#julia = Float64Array, python = 'list', Vektor der Länge nbpoints (symmetrisch)

file_pot=open("pot_at_int_points.dat", "w")
for i in range(0, nbpoints):
   file_pot.write( str(len*points[i]) + "  " + str( potval[i]) + "  " + str( potval[i]+0.5*force*(len*points[i])**2  ) + "\n")
file_pot.close()


# build potential part of Hamilton matrix:
perpotmat = []
for i in range(nbfcts):
	zeile = []
	for j in range(nbfcts):
		zeile += [0.0]
	perpotmat += [zeile]
# leere Matrix, julia = Array von Float64, python = list von list


for i in range(nbfcts):
	for j in range(i+1):
		integrand = []
		for l in range(nbpoints):
			integrand += [ 0.0 ]
		for k in range(nbpoints):  
			a = hvalues[k][i] * hvalues[k][j] * potval[k]
			integrand[k] = a
		b = np.dot(weights,integrand) # Punktprodukt der Vektoren 
		perpotmat[i][j] = b
		perpotmat[j][i] = b


# build full Hamilton matrix:
hamiltonmat = perpotmat.copy()
omega = sqrt(force/mass)
for i in range(0, nbfcts): 
   hamiltonmat[i][i] = hamiltonmat[i][i] + (i+0.5)*omega


# determine eigenvalues and eigenvectors of Hamilton matrix:
energies, coefficients = np.linalg.eig(hamiltonmat)
name = "energies_pdist" + str(pdist)+"_odist" + str(odist) + ".dat"
file_en=open(name, "w")
for i in range(nbfcts):
   file_en.write( str(i) + "  " + str( energies[i]) + "\n") 
file_en.close()





