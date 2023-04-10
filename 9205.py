import sys
from collections import deque

def check_dist(x,y,tx,ty):
    dist = abs(tx-x) + abs(ty-y)
    if dist > 1000 : return False
    else : return True

def BFS(graph,N,V):
    queue = deque()
    visited = [False] * N

    queue.append(V)
    visited[0] = True

    while queue :
        tmp = queue.popleft()
        x,y = graph[tmp][0], graph[tmp][1]
        for i in range(N):
            if not visited[i] and check_dist(x,y,graph[i][0],graph[i][1]):
                queue.append(i)
                visited[i] = True
    # print(visited)
    if visited[-1] : return True
    else : return False

for _ in range(int(input())):
    cu = int(input())
    spot = [[0,0]for _ in range(cu+2)]
    for i in range(0,cu+2):
        spot[i][0],spot[i][1] = map(int,input().split())
    
    # print(spot)
    print("happy" if BFS(spot,cu+2,0) else "sad")