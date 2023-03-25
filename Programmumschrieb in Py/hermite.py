def sqrt(x):
	return ( x ** (1/2) ) 

import math
pi = math.pi

def norm_hermite_polynomials_at_x(n,x):
	# returns a vector containig the Hermite polynomials up to degree n
	# evaluated at argument x
	h = []
	for k in range(n+1):
		h += [0.0] #(0.0,n+1)
	#print(h, len(h)) 
	h[0] = 1/sqrt(sqrt(pi))
	#print(h)
	if n == 0: 
		return h
	else:
		h[1] = sqrt(2)*x*h[0]
	if n == 1: 
		return h
	else:
		#print(h)
		for i in range(2,n+1): # inklusive 2 (3. Position) & inklusive n+1 
			#print("i", i)
			#j = i + 1 #2
			h[i] = sqrt(2/i ) * x * h[i-1] - sqrt((i-1)/i) * h[i-2]
			#h[i] = sqrt(2/(j-1))*x*h[i-1] - sqrt((j-2)/(j-1))*h[i-2]
			#print("Term 1: ", math.sqrt(2/(j-1))*x, "Term 2: ", sqrt((j-2)/(j-1)) ) 
		return h
	return 


#print( norm_hermite_polynomials_at_x(10, 10 ), ";",   norm_hermite_polynomials_at_x(5, 2 ) ) 
