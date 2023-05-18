n = 5
INF = float('inf')
adj = [[0,5,0,9,1],[5,0,2,0,0],[0,2,0,7,0],[9,0,7,0,2],[1,0,0,2,0]]
dist = [[INF for _ in range(n)]for _ in range(n)]
next_node = [[-1 for _ in range(n)]for _ in range(n)]

def print_graph(graph):
    for row in graph :
        for el in row :
            if el != INF :
                print(el,end=' ')
            else : print('I',end=' ')
        print()
    print("=================================")

for i in range(n):
    for j in range(n):
        if i == j : 
            dist[i][j] = 0
        elif adj[i][j] != 0:
           dist[i][j] = adj[i][j]
        else :
            dist[i][j] = INF

print("BASE")
print_graph(dist)

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if dist[i][j] > dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = k
    print_graph(dist)

def find_path(start, end):
    if next_node[start][end] == -1:
        return
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    print(path)

print("Shortest Path Distances:")
print_graph(dist)

print("Shortest Path from 0 to 4:")
path = find_path(0, 2)  # 0번 노드에서 4번 노드로 가는 경로