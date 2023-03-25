using FastGaussQuadrature
using SpecialFunctions
using LinearAlgebra

# read technical detail parameters from file "tecdetails.inp":
include("TecDetails.jl")

# read physical system parameters from file "systems.inp":
include("SystemParam.jl")

# provide "normalized" Hermite polynomials :
include("normhermitepoly.jl")

# provide wavefunction and energy calculation methods:
include("PTMatEl.jl")

#open output files: append or write 
if isfile("eigenvalues.tab") 
	fileEval = open("eigenvalues.tab","a")
	println("\n") 
else	
	fileEval = open("eigenvalues.tab","w")
	println(fileEval, "#mass\tfConst\trSep\txDist\tzDist\tnbFcts\tnbGHpoints\tnbEigval\tmxPTord\teigenvalues")
end

if isfile("contributions.tab") 
	fileContrib = open("contributions.tab","a")
	println("\n") 
else
	fileContrib = open("contributions.tab","w")
	println(fileContrib, "#mass\tfConst\trSep\txDist\tzDist\tnbFcts\tnbGHpoints\tnbEigval\tmxPTord\tcontributions")
end


for itec = 1:nbtec
    
    # obtain Gauss-Hermite quadrature points and weights:
    points, weights = gausshermite(details[itec].nbGHpoints)

    for isys = 1:nbsys

        # zeroth order Hamilton matrix elements:
        H0mat = zeros(details[itec].nbFcts)
        omega = sqrt(systems[isys].fConst/systems[isys].mass)
        for i = 1:details[itec].nbFcts
           H0mat[i] = omega*(i-0.5)
        end
        open("H0matrix.tab","w") do io
            writedlm(io, H0mat)
        end

        # calculate potential at quadrature points:
        len = 1/sqrt(sqrt(systems[isys].fConst*systems[isys].mass))
        r(x) = sqrt((systems[isys].zDist)^2+(systems[isys].xDist-sqrt(2)*len*x)^2)
        pot(x) = erf(systems[isys].rSep*r(x))/r(x)
        potval=pot.(points)
        totpot(x) = pot(x) + 0.5*systems[isys].fConst*(len*x)^2
        totval=totpot.(points)
        open("potvalues.tab","w") do io
            println(io, "# force constant = ", systems[isys].fConst,
			" ; mass = ", systems[isys].mass,
			" ; range separation parameter = ", systems[isys].rSep,
			" ; xDist = ", systems[isys].xDist,
			" ; zDist = ", systems[isys].zDist)
            println(io, "#x\tperturbation potential\ttotal potential")
            writedlm(io, [points.*len potval totval], "\t")
        end

        # calculate (normalized) Hermite polynomials at quadrature points:
        hvalues = normhermitepoly.(details[itec].nbFcts,points)

        # perturbation potential matrix elements:
        perpotmat = zeros(div(details[itec].nbFcts*(details[itec].nbFcts+1),2))
        ij = 0
        for i = 1:details[itec].nbFcts
            for j = i:details[itec].nbFcts
                ij += 1
                integrand = zeros(details[itec].nbGHpoints)
                for k = 1:details[itec].nbGHpoints
                    integrand[k] = hvalues[k][i] * hvalues[k][j] * potval[k]
                end
                perpotmat[ij] = dot(weights,integrand)
            end
        end
        open("pertmatrix.tab","w") do io
            writedlm(io, perpotmat)
        end
        #println( H0mat, "\n\n", perpotmat) 
        Hamiltonian = PTMatEl(H0mat,perpotmat)
        #println(Hamiltonian) 
        # determine "exact" ground state energy and wavefunction
        eigval, eigvec = ExactWfn(Hamiltonian)
        print(fileEval, systems[isys].mass, "\t", systems[isys].fConst, "\t",systems[isys].rSep, "\t")
        print(fileEval, systems[isys].xDist, "\t", systems[isys].zDist, "\t",)
        print(fileEval, details[itec].nbFcts, "\t", details[itec].nbGHpoints, "\t")
        print(fileEval, details[itec].nbEigval, "\t", details[itec].mxPTord)
        for n = 1:min(details[itec].nbEigval,details[itec].nbFcts)
            print(fileEval, "\t",eigval[n])
        end
        print(fileEval, "\n")

        # determine perturbation contributions to ground state energy and wavefunction
        energycontrib, veccontrib = RSPTWfn(Hamiltonian,details[itec].mxPTord)
        print(fileContrib, systems[isys].mass, "\t", systems[isys].fConst, "\t",systems[isys].rSep, "\t")
        print(fileContrib, systems[isys].xDist, "\t", systems[isys].zDist, "\t",)
        print(fileContrib, details[itec].nbFcts, "\t", details[itec].nbGHpoints, "\t")
        print(fileContrib, details[itec].nbEigval, "\t", details[itec].mxPTord)
        print(fileContrib, "\t",H0mat[1])
        for n = 1:details[itec].mxPTord
            print(fileContrib, "\t",energycontrib[n])
        end
        print(fileContrib, "\n")

    end
end

close(fileEval)
close(fileContrib)
