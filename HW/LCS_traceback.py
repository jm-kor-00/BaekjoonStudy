def lcs_dp_traceback(X,Y,L):
    lcs = ""
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j-1] and v > L[i-1][j] and v > L[i-1][j-1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs
        
        elif v == L[i][j-1] and v > L[i-1][j]: j-= 1
        else : i -= 1
    
    return lcs