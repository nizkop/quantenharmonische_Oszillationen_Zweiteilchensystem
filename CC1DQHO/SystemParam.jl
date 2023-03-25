struct SystemParam
    mass::Float64
    fConst::Float64
    rSep::Float64
    xDist::Float64
    zDist::Float64
end

using DelimitedFiles
sys, syshead = readdlm("systems.inp",header=true)
nbsys = size(sys)[1]
systems = Array{SystemParam,1}(undef,nbsys)
for i = 1:nbsys
    systems[i] = SystemParam(sys[i,1],sys[i,2],sys[i,3],sys[i,4],sys[i,5])
end
