struct TecDetails
    nbFcts::Int
    nbGHpoints::Int
    nbEigval::Int
    mxPTord::Int
end

using DelimitedFiles
tec, techead = readdlm("tecdetails.inp",header=true)

nbtec = size(tec)[1]

details = Array{TecDetails,1}(undef,nbtec)
for i = 1:nbtec
    details[i] = TecDetails(tec[i,1],tec[i,2],tec[i,3],tec[i,4])
end
