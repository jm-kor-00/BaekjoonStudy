import sys
def dvq(A,B,C):
    if B == 1:
        return A % C
    
    D = dvq(A,B//2,C)

    if B % 2 == 1:
        return (D * D % C) * A % C
    else :
        return (D*D) % C

A, B, C = map(int,sys.stdin.readline().split())
print(dvq(A,B,C))