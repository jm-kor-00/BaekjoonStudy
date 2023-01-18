import sys
input = sys.stdin.readline

N = int(input())
C = list(map(int,input().split()))
DP = [0] * N

if N == 1 :
    DP[0] = C[0]
elif N > 1 :
    DP[0] = C[0]
    DP[1] = max(C[0] * 2, C[1])

for i in range(2,N):
    DP[i] = C[i]
    for j in range(0,i):
        if DP[i] < DP[i - (j + 1)] + C[j]:
            DP[i] = DP[i - (j + 1)] + C[j]
    # print(i,"->",DP[i])
print(DP[N - 1])