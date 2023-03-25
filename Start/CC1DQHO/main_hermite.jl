include("hermite_polynomials_at_x.jl")
x=collect(LinRange(-5.0, +5.0, 201))
H=hermite_polynomials_at_x.(9,x)
Herm0 = fill(0.0,201)
Herm1 = fill(0.0,201)
Herm2 = fill(0.0,201)
Herm3 = fill(0.0,201)
Herm4 = fill(0.0,201)
Herm5 = fill(0.0,201)
Herm6 = fill(0.0,201)
Herm7 = fill(0.0,201)
Herm8 = fill(0.0,201)
Herm9 = fill(0.0,201)
for i =1:201
   Herm0[i] = H[i][1]
   Herm1[i] = H[i][2]
   Herm2[i] = H[i][3]
   Herm3[i] = H[i][4]
   Herm4[i] = H[i][5]
   Herm5[i] = H[i][6]
   Herm6[i] = H[i][7]
   Herm7[i] = H[i][8]
   Herm8[i] = H[i][9]
   Herm9[i] = H[i][10]
   println(x[i]," ",Herm0[i]," ",Herm1[i]," ",Herm2[i]," ",Herm3[i]," ",Herm4[i], " ",Herm5[i]," ",Herm6[i]," ",Herm7[i]," ",Herm8[i]," ",Herm9[i])
end
~                                                                                       
