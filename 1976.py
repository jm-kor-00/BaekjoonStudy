import sys
from collections import deque
input = sys.stdin.readline

def BFS(N,S,D,graph):
        visited = [False for i in range(N)]
        que = deque()
        que.append(S)
        visited[S] = True
        while que:
            t = que.popleft()
            if t == D : return True
            for d in range(N):
                if visited[d] : continue
                if graph[t][d] == 0 : continue
                que.append(d)
                visited[d] = True
        return False

def solution():
    N = int(input())
    M = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    
    order = list(map(int,input().split()))
    for i in range(M):
        order[i] -= 1

    for i in range(M-1):
        if not BFS(N,order[i],order[i+1],graph):
            return False
    return True

if solution():
    print("YES")
else :
    print("NO")