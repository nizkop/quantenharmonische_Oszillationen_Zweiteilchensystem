struct PTMatEl
    H0El::Vector # diagonal matrix elements only (H0 should be diagonal)
    VEl::Vector  # upper triangle only (V should be hermitian)
end

# This function calculates the ground state RSPT wavefunction corrections up to
# "WfnOrder" and, as a byproduct, the RSPT energy corrections up to "WfnOrder+1"
function RSPTWfn(PTMatEl, WfnOrder::Int)

    dim = length(PTMatEl.H0El)
    if dim == 1 error("H0 and V matrices must be larger than 1-dimensional") end
    if length(PTMatEl.VEl) != dim*(dim+1)/2
        error("dimension mismatch between H0 and V")
    end
    if WfnOrder < 1 error("perturbation wavefunction order must at least be 1") end
    
    V00 = PTMatEl.VEl[1]

    VVec = zeros(dim-1)
    EpsInv = zeros(dim-1)
    for i = 2:dim
        VVec[i-1] = PTMatEl.VEl[i]
        EpsInv[i-1] = 1/(PTMatEl.H0El[i]-PTMatEl.H0El[1])
    end

    VMat = zeros(dim-1,dim-1)
    k = dim
    for i = 2:dim
        for j = i:dim
            VMat[i-1,j-1] = PTMatEl.VEl[k+=1]
            VMat[j-1,i-1] = conj(VMat[i-1,j-1])
        end
    end

    PTCoeff = zeros(dim-1,WfnOrder)
    PTEnerg = zeros(WfnOrder+1)
    PTCoeff[:,1] = -EpsInv.*VVec
    PTEnerg[1] = V00
    PTEnerg[2] = VVec'*PTCoeff[:,1]
    if WfnOrder >= 2
        for n = 2:WfnOrder
            PTCoeff[:,n] = -VMat*PTCoeff[:,n-1]
            for m = 1:n-1
                PTCoeff[:,n] += PTEnerg[m]*PTCoeff[:,n-m]
            end
            PTCoeff[:,n] = EpsInv.*PTCoeff[:,n]
            PTEnerg[n+1] = VVec'*PTCoeff[:,n]
        end
    end

    return PTEnerg, PTCoeff
end

# This function calculates "exact" wavefunctions and energies as
# eigenvectors and eigenvalues of H0+V
function ExactWfn(PTMatEl)

    dim = length(PTMatEl.H0El)
    if dim == 1 error("H0 and V matrices must be larger than 1-dimensional") end
    if length(PTMatEl.VEl) != dim*(dim+1)/2
        error("dimension mismatch between H0 and V")
    end

    HMat = zeros(dim,dim)
    k=0
    for i = 1:dim
        for j = i:dim
            HMat[i,j] = PTMatEl.VEl[k+=1]
            HMat[j,i] = conj(HMat[i,j])
        end
        HMat[i,i] += PTMatEl.H0El[i]
    end
    
    EigenValues = eigvals(HMat)
    EigenVectors = eigvecs(HMat)
    return EigenValues, EigenVectors
end
