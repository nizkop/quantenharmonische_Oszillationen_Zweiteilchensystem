using LinearAlgebra
using FastGaussQuadrature

# physical parameters:
pdist = 0.0    # parallel distance between the oscillators (in a.u.)
odist = 20.0    # orthogonal distance between the oscillators (in a.u.)
mass = 1.0     # mass of oscillating particle (in a.u.)
force =1.0    # force constant (in a.u.)

# technical parameters:
nbpoints = 200 # number of Gauss-Hermite integration points
nbfcts = 50    # number of QHI eigenfunctions to be used

points, weights = gausshermite(nbpoints) # obtain Gauss-Hermite qudrature points and weights

# calculate (normalized) Hermite polynomials at quadrature points:
include("norm_hermite_polynomials_at_x.jl")
hvalues=norm_hermite_polynomials_at_x.(nbfcts,points)

# calculate potential at quadrature points:
len = 1/sqrt(force*mass)
pot(x) = 1/sqrt(odist^2+(pdist-len*x)^2)
potval=pot.(points)
file_pot=open("pot_at_int_points.dat", "w")
for i = 1:nbpoints
   println(file_pot, len*points[i], "  ", potval[i], "  ", potval[i]+0.5*force*(len*points[i])^2)
end
close(file_pot)

# build potential part of Hamilton matrix:
perpotmat = zeros(nbfcts,nbfcts)
for i = 1:nbfcts
   for j = 1:i
      integrand = zeros(nbpoints)
      for k = 1:nbpoints
         integrand[k] = hvalues[k][i] * hvalues[k][j] * potval[k]
      end
      perpotmat[i,j] = dot(weights,integrand)
      perpotmat[j,i] = perpotmat[i,j]
   end
end

# build full Hamilton matrix:
hamiltonmat = copy(perpotmat)
omega = sqrt(force/mass)
for i = 1:nbfcts
   hamiltonmat[i,i] = hamiltonmat[i,i] + ((i-1)+0.5)*omega
end

# determine eigenvalues of Hamilton matrix:
energies = eigvals(hamiltonmat)
file_en=open("energies.dat", "w")
for i = 1:nbfcts
   println(file_en, i, "  ", energies[i])
end
close(file_pot)

# determine eigenvectors of Hamilton matrix:
coefficients = eigvecs(hamiltonmat)
