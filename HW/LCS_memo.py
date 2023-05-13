def lcs_memo(X, Y, i, j, memo):
    if i == 0 or j == 0:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if X[i-1] == Y[j-1]:
        memo[(i, j)] = 1 + lcs_memo(X, Y, i-1, j-1, memo)
    else:
        memo[(i, j)] = max(lcs_memo(X, Y, i-1, j, memo), lcs_memo(X, Y, i, j-1, memo))

    return memo[(i, j)]