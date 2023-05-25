graph = [[0,1,0,0,1,0],
        [1,0,1,0,1,0],
        [0,1,0,1,0,0],
        [0,0,1,0,1,1],
        [1,1,0,1,0,0],
        [0,0,0,1,0,1]]

N = len(graph)
visited = [False] * N

def DFS(V):
    global visited
    global graph
    visited[V] = True
    print(V + 1, end = ' -> ')
    for i in range(0,N,1):
        if graph[V][i] == 1 and not visited[i] :
            DFS(i)
            
DFS(0)