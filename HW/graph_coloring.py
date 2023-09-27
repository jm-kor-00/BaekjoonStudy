def isSafe(g,v,c,color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False
    return True

def DFS_graph_coloring(graph,k,v,color):
    if v == len(graph):
        return True
    
    for c in range(1,k+1):
        if isSafe(graph,v,c,color):
            color[v] = c
            if DFS_graph_coloring(graph,k,v+1,color):
                return True
            color[v] = 0

    return False

def graphColoring(graph,k,states):
    color = [0] * len(graph)
    ret = DFS_graph_coloring(graph,k,0,color)
    if ret :
        for i in range(len(graph)):
            print("%3s = "%states[i], color_name[color[i]])
    else :
        print("그래프를 색칠할 수 없음")

states = ['NT','WA','Q','SA','NSW','V']
color_name = ["none","빨","주","노","초","파"]

g = [[0,1,1,1,0,0],
     [1,0,0,1,0,0],
     [1,0,0,1,1,0],
     [1,1,1,0,1,1],
     [0,0,1,1,0,1],
     [0,0,0,1,1,0]]

g2 = [[0,1,0,0],
      [1,0,1,1],
      [0,1,0,1],
      [0,1,1,0]]

g3 = [[1,1,1],
      [1,0,0],
      [1,0,0]]

print("##############################")
print("graph1 : \n")
print("색상 3개:")
graphColoring(g,3,states)
print("색상 2개:")
graphColoring(g,2,states)

print("##############################")
print("graph2 : \n")
print("색상 3개:")
graphColoring(g2,3,states)
print()
print("색상 2개:")
graphColoring(g2,2,states)

print("##############################")
print("graph3 : \n")
print("색상 3개:")
graphColoring(g3,3,states)
print()
print("색상 2개:")
graphColoring(g3,2,states)