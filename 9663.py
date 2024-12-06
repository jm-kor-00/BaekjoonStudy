from copy import deepcopy
N = int(input())
row = [0] * N
res = 0

def isOnCross(x,y,a,b):
    if abs((x-a) / (y-b)) == 1: return True
    return False

def isOK(n):
    for i in range(n):
        if row[i] == row[n]: return False
        if isOnCross(i,row[i],n,row[n]) : return False
    return True

def recur(count):
    global res,N
    if count == N:
        res+=1; return
    for i in range(N):
        #count번째는 i열에 있다.
        row[count] = i
        if isOK(count):
            recur(count+1)

recur(0)
print(res)