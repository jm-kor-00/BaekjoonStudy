import sys
input = sys.stdin.readline

cost = []
N = int(input())
for _ in range(N):
    cost.append(list(map(int,input().split())))

DP = [[0 for _ in range(3)]for _ in range(N)]
DP[0] = cost[0]
for i in range(1,N):
    DP[i][0] = min(DP[i-1][1],DP[i-1][2]) + cost[i][0]
    DP[i][1] = min(DP[i-1][0],DP[i-1][2]) + cost[i][1]
    DP[i][2] = min(DP[i-1][0],DP[i-1][1]) + cost[i][2]

print(min(DP[N-1]))