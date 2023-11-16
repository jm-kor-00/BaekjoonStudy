import sys
from collections import deque
input = sys.stdin.readline

def BFS(S:int,D:int,visited:dict,line:list,G:dict)->int:
    que = deque()
    que.append((S,0))
    visited[S] = True
    while que:
        node,dist = que.popleft() # ex) node : 303 , dist : 0
        tmp = G[node] # ex) tmp : [1,2]
        for cLine in tmp: # ex) cLine : 1
            for nxt in line[cLine]: # ex) nxt : 300
                if nxt == D : 
                    return dist + 1
                if not visited[nxt]:
                    que.append((nxt,dist + 1))
                    visited[nxt] = True
        # print(que)

    return (-77)

for _ in range(int(input())):
    line = []
    for _ in range(int(input())):
        b = int(input())
        line.append(list(map(int,input().split())))

    start = int(input())
    dest = int(input())

    busDict = {} #노선 표시할 딕셔너리
    visited = {} #방문여부 표시할 딕셔너리

    for i in range(len(line)):
        for el in line[i]:
            visited[el] = False #그냥 반복문 돌리는 김에 visited도 돌림
            if el in busDict:
                busDict[el].append(i)
            else :
                busDict[el] = [i]

    print(line)
    print(busDict)
    print(visited)

    #출발도착 일치
    if start == dest :
        print(0)
    #출발지가 노선에 없을 경우
    elif not start in busDict:
        print(-77)

    else :
        print(BFS(start,dest,visited,line,busDict))