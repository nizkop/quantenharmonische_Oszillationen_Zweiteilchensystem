#Inhalte linearer ALgebra:
import numpy as np

#Gaus-Quadratur:
import scipy
#from scipy.integrate import fixed_quad, quadrature



# physical parameters:
pdist = 0.0    # parallel distance between the oscillators (in a.u.)
odist =  0.0 	# orthogonal distance between the oscillators (in a.u.)
mass =  1.0     # mass of oscillating particle (in a.u.)
force =  1.0    # force constant (in a.u.)



# technical parameters:
nbpoints = 2 # number of Gauss-Hermite integration points
nbfcts = 5   # number of QHI eigenfunctions to be used

points, weights = np.polynomial.hermite.hermgauss(nbpoints) 
#gausshermite(nbpoints) # obtain Gauss-Hermite quadrature points and weights
# type liefert: <class 'tuple'> aus 2 Elementen der Art <class 'numpy.ndarray'>

#print(points)
# [-5.387480890011233, -4.603682449550744, -3.9447640401156265, -3.3478545673832163, -2.7888060584281296, -2.2549740020892757, -1.7385377121165857, -1.2340762153953255, -0.7374737285453978, -0.24534070830090382, 0.24534070830090382, 0.7374737285453978, 1.2340762153953255, 1.7385377121165857, 2.2549740020892757, 2.7888060584281296, 3.3478545673832163, 3.9447640401156265, 4.603682449550744, 5.387480890011233])
#print(weights)
# [2.2293936455341583e-13, 4.399340992273223e-10, 1.0860693707692783e-7, 7.802556478532184e-6, 0.00022833863601635774, 0.0032437733422378905, 0.024810520887463966, 0.10901720602002457, 0.28667550536283243, 0.4622436696006102, 0.4622436696006102, 0.28667550536283243, 0.10901720602002457, 0.024810520887463966, 0.0032437733422378905, 0.00022833863601635774, 7.802556478532184e-6, 1.0860693707692783e-7, 4.399340992273223e-10, 2.2293936455341583e-13]


# calculate (normalized) Hermite polynomials at quadrature points:
from hermite import * #File: hermite.py
#hvalues (original = Array{Array{Float64,1},1} ; Länge 20, Länge 1. Element = 6) 
# hvalues=norm_hermite_polynomials_at_x.(nbfcts,points)
hvalues = []
for i in range(nbpoints): # len(points) 
		hvalues.append( norm_hermite_polynomials_at_x(nbfcts,points[i]) ) # für "import hermite" hier "hermite." vorm Funktionsaufruf
#print("hvalues ", hvalues)#, len(hvalues), len(hvalues[0]) ) # !? 

# calculate potential at quadrature points:
len = 1/sqrt(force*mass)
def pot(x):
	return 1/sqrt((odist**2)+((pdist-len*x)**2))
potval=[]
#print(type(points), points)
for i in range(nbpoints): # da nbpoints = len(points)
	potval += [pot(points[i])]
#print(potval,  type(potval))
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

#print("potval ", potval)
#hvalues = [[0.7511255444649425, -0.7511255444649427, 1.1102230246251565e-16, 0.6132914389031022, -0.3066457194515513, -0.41140840422179853], [0.7511255444649425, 0.7511255444649427, 1.1102230246251565e-16, -0.6132914389031022, -0.3066457194515513, 0.41140840422179853]]
#hvalues = [[0.0, 0.1, 0.2, 0.3, 0.4, 0.5], [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]]


for i in range(nbfcts):
	for j in range(i+1):
		integrand = []
		#print("integrand neu", integrand)
		for l in range(nbpoints):
			integrand += [ 0.0 ]
		#print("integrand", integrand)
		for k in range(nbpoints):  
			a = hvalues[k][i] * hvalues[k][j] * potval[k]
			integrand[k] = a
			#print("i: ", i+1, ", j : ", j+1, ", k: ", k+1) 
			#print("a ", a, ", potval[k] ", potval[k])
			#print("	, hvalues[k][i] ", hvalues[k][i], ", hvalues[k][j] ", hvalues[k][j]) 
		#print("perpotmat", perpotmat, "weights", weights, "integrand", integrand)
		b = np.dot(weights,integrand)
		#print("b ", b) 
		perpotmat[i][j] = b
		#print("nach dot ", perpotmat)
		perpotmat[j][i] = b
print("perpotmat Ende ", perpotmat) 



# build full Hamilton matrix:
hamiltonmat = perpotmat.copy()
omega = sqrt(force/mass)
for i in range(0, nbfcts): 
   hamiltonmat[i][i] = hamiltonmat[i][i] + (i+0.5)*omega
print(hamiltonmat) 



# determine eigenvalues of Hamilton matrix:
energies, coefficients = np.linalg.eig(hamiltonmat)

#energies = eigvals(hamiltonmat)
name = "energies_pdist" + str(pdist)+"_odist" + str(odist) + ".dat"
file_en=open(name, "w")
for i in range(nbfcts):
   file_en.write( str(i) + "  " + str( energies[i]) + "\n") 
file_en.close()

# determine eigenvectors of Hamilton matrix:
#coefficients = eigvecs(hamiltonmat)

print(coefficients) 



