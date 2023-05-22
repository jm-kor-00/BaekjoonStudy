def print_Adjlist(graph):
    print("==========================")
    for i in range(len(graph)):
        print(i+1,end=' -> ')
        for el in graph[i] :
            print(el+1,end=', ')
        print()
    print("==========================")

class Node : #Link List에 사용하는 노드클래스, 참고만
    #생성자
    def __init__(self,n_data,link=None):
        self.data = n_data
        self.link = link
    
#파이썬의 리스트는 말단삽입(append)를 지원하므로
#2차원 리스트로 인접리스트 표현을 구현할 수 있다.
#간선만 나타내므로, 희소그래프에서 유용하다.

#case1
#삽입되는 순서는 중요하지 않음
G = [[1,4], #1번노드
     [0,2,4], #2
     [1,3], #3
     [2,4,5], #4
     [0,1,3], #5
     [3]] #6

print_Adjlist(G)

#case2
N = 6 #노드 개수
Graph = [[] for _ in range(N)]
for _ in range(int(input('간선의 개수 : '))):
    u, v = map(int,input('인접한 두 정점 입력 ex) 1 2 : ').split())
    u -= 1; v -= 1 #노드번호 맞추기 위해서 -1
    #새로운 간선 정보를 삽입
    Graph[u].append(v)
    Graph[v].append(u)

print_Adjlist(Graph)