from collections import deque
import sys
input = sys.stdin.readline

def Topological_Sort(N,graph,indegree):
    queue = deque()
    step = []
    lev = 0

    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        for _ in range(len(queue)):
            tmp = queue.popleft()
            step.append(tmp)
            for i in range(N+1):
                if graph[tmp][i] == 1 :
                    indegree[i] -= 1
                    if indegree[i] == 0 :
                        queue.append(i)
        lev += 1
    return step

for _ in range(int(input())):
    N, K = map(int,input().split())
    DP = [0 for _ in range(N+1)]
    build = list(map(int,input().split()))
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    indegree = [0 for _ in range(N + 1)]
    for _ in range(K):
        f,a = map(int,input().split())
        graph[f][a] = 1
        indegree[a] += 1
    W = int(input())

    step = Topological_Sort(N,graph,indegree)
    
    for el in step:
        max = 0
        for j in range(N+1):
            if graph[j][el] :
                if max < DP[j] : max = DP[j] 
        DP[el] = max + build[el - 1]

    print(DP[W])