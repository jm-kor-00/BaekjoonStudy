import sys
input = sys.stdin.readline

def fromTop(A,index):
    count = 0
    biggest = A[index]
    for i in range(index,0,-1):
        if biggest > A[i - 1] : 
            count += 1
            biggest = A[i - 1]
    return count + 1

N = int(input())
A = list(map(int,input().split()))

max = [1,A[0],A[0]] #val,smallest,max

for i in range(1,N):
    if A[i] > A[max[1]] :
        tmp = fromTop(A,i)
        if tmp > max[0] :
            max = [tmp,i]
print(max[0])