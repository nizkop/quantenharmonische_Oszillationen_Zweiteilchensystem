include("qho1d_eigfcts_at_x.jl")
x=collect(LinRange(-5.0, +5.0, 201))
mass=2
force=1
P=qho1d_eigfcts_at_x.(9,mass,force,x)
Psi0 = fill(0.0,201)
Psi1 = fill(0.0,201)
Psi2 = fill(0.0,201)
Psi3 = fill(0.0,201)
Psi4 = fill(0.0,201)
Psi5 = fill(0.0,201)
Psi6 = fill(0.0,201)
Psi7 = fill(0.0,201)
Psi8 = fill(0.0,201)
Psi9 = fill(0.0,201)
for i =1:201
   Psi0[i] = P[i][1]
   Psi1[i] = P[i][2]
   Psi2[i] = P[i][3]
   Psi3[i] = P[i][4]
   Psi4[i] = P[i][5]
   Psi5[i] = P[i][6]
   Psi6[i] = P[i][7]
   Psi7[i] = P[i][8]
   Psi8[i] = P[i][9]
   Psi9[i] = P[i][10]
   println(x[i]," ",Psi0[i]," ",Psi1[i]," ",Psi2[i]," ",Psi3[i]," ",Psi4[i], " ",Psi5[i]," ",Psi6[i]," ",Psi7[i]," ",Psi8[i]," ",Psi9[i])
end
~                                                                                       
