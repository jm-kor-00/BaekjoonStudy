import sys
input = sys.stdin.readline

N = int(input())
graph = [[float('inf') for _ in range(N)]for _ in range(N)]
for _ in range(int(input())):
    a,b,w = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],w)

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(N):
    for j in range(N):
        t = graph[i][j]
        if t == float('inf') or i==j :
            t = 0
        print(t,end=' ')
    print()