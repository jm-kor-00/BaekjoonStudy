#0-1 knapsack problem
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
items = []
for _ in range(N):
    items.append(list(map(int,input().split())))
print(items)
for i in range(N):
    weight = items[i][0]
    value = items[i][1]
    for j in range(K):
        if j < weight :
            