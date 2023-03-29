def SELF(N):
    if N == 0 : return 0
    elif N == 1 : return 1
    else :
        return SELF(N-2) * SELF(N-1) + SELF(N-1)
print(SELF(4))