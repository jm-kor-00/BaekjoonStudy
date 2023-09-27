#0-1 knapsack problem
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
items = []
for _ in range(N):
    items.append(list(map(int,input().split())))

knapsack = [[0 for _ in range(K+1)] for _ in range(N)]

#물건이 N
for i in range(N):
    #각물건 무게, 가치
    weight = items[i][0]
    value = items[i][1]

    for j in range(K+1):
        #무게, K가 최대무게 
        if j < weight :
            knapsack[i][j] = knapsack[i-1][j]
        else :
            knapsack[i][j] = max(knapsack[i-1][j], value + knapsack[i-1][j-weight])

print(knapsack[N-1][K])