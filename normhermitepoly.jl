function normhermitepoly(n,x)
# returns a vector containing the Hermite polynomials up to degree n
# evaluated at argument x
   h = fill(0.0,n+1)
   h[1] = 1/sqrt(sqrt(pi))
   if n == 0 return h
   else
      h[2] = sqrt(2)*x*h[1]
      if n==1 return h
      else
         for i = 3:n+1
            h[i] = sqrt(2/(i-1))*x*h[i-1]-sqrt((i-2)/(i-1))*h[i-2]
         end
         return h
      end
   end
end
