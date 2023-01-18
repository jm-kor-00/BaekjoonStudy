import sys
input = sys.stdin.readline
N,K = map(int,input().split())

DP = [[0 for j in range(K + 1)] for i in range(N + 1)]

for n in range(N + 1):
    DP[n][0] = 0 
    DP[n][1] = 1

for i in range(N + 1) :
    for k in range(2,K + 1):
        for n in range(i + 1):
            DP[i][k] += DP[i - n][1] * DP[n][k - 1]
print(DP[N][K] % 1000000000)