
#Inhalte linearer ALgebra:
import numpy as np

a = np.array([[3, 1], [2, 2]])
w, v = np.linalg.eig(a)

print(w)
print(v)





#Gaus-Quadratur:
import scipy
from scipy.integrate import fixed_quad, quadrature

f = lambda x: x**2

fixed_quad(f, 0, 1)
#(0.33333333333333326, None)

print( quadrature(f, 0, 1) )

