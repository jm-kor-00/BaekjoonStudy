from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[]for _ in range(N+1)]

for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    for j in range(1,len(tmp) - 2, 2):
        graph[tmp[0]].append((tmp[j],tmp[j+1]))

def BFS(N,V):
    queue = deque()
    visited = [-1] * (N+1)
    
    queue.append(V)
    visited[V] = 0
    far_node, far_dist = V, 0
    
    while queue:
        tmp = queue.popleft()
        for node,dist in graph[tmp]:
            if visited[node] == -1:
                visited[node] = visited[tmp] + dist
                queue.append(node)
                if far_dist < visited[node]:
                    far_node,far_dist = node, visited[node]
    return far_node, far_dist

nxt,dist = BFS(N,1)
fin,res = BFS(N,nxt)
print(res)