function qho1d_eigfcts_at_x(n,mass,force,x)
# Returns a vector containig the one-dimensional Quantum Harmonic Oscillator
# eigenfunctions up to quantum number n evaluated at argument x.
# Mass (mass) and force constant (force) to be given in atomic units.
   alpha = sqrt(force*mass)
   len = 1/sqrt(alpha)
   xi = x/len
   psi = fill(0.0,n+1)
   psi[1] = exp(-xi^2/2)/sqrt(len*sqrt(pi))
   if n == 0 return psi
   else
      psi[2] = sqrt(2)*xi*psi[1]
      if n==1 return psi
      else
         for i = 3:n+1
            psi[i] = sqrt(2/(i-1))*xi*psi[i-1]-sqrt((i-2)/(i-1))*psi[i-2]
         end
         return psi
      end
   end
end
