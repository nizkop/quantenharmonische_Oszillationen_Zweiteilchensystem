function hermite_polynomials_at_x(n,x)
# returns a vector containig the Hermite polynomials up to degree n
# evaluated at argument x
   h = fill(0.0,n+1)
   h[1] = 1
   if n == 0 return h
   else
      h[2] = 2x
      if n==1 return h
      else
         for i = 3:n+1
            h[i] = 2*x*h[i-1]-2*(i-2)*h[i-2]
         end
         return h
      end
   end
end
