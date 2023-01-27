import sys
input = sys.stdin.readline

n, r, c = map(int,input().split())

def Zfunction(n,r,c):
    total = 0
    N,R,C = n,r,c
    if N == 1:
        total = r + C
        if R == 1 : 
            total += 1
        return total
    else :
        if C >= 2 ** (N-1):
            if R >= 2 ** (N-1):
                total += (((2 ** (N - 1)) ** 2) * 3)
                C -= 2 ** (N-1)
                R -= 2 ** (N-1)
            else :
                total += (((2 ** (N - 1)) ** 2) * 1)
                C -= 2 ** (N-1)
        else :
            if R >= 2 ** (N-1):
                total += (((2 ** (N - 1)) ** 2) * 2)
                R -= 2 ** (N-1)
            else :
                pass
    return total + Zfunction(N - 1,R,C)

print(Zfunction(n,r,c))