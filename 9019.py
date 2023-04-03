import sys
from collections import deque
input = sys.stdin.readline

def BFS(init,goal):
    queue = deque()
    visited = [False] * 10000
    queue.append((init,""))
    while queue :
        #큐에 있는 수와 기록 pop
        num,record = queue.popleft()
        if num == goal : return record

        for act in ('D','S','L','R'):
            tmp = num
            if act == 'D':
                tmp = (2 * tmp) % 10000 #D 연산 수행
            elif act == 'S':
                tmp = (tmp - 1) % 10000 #1감소
            elif act == 'L':
                tmp = (tmp % 1000) * 10 + tmp // 1000
            else : 
                tmp = (tmp % 10) * 1000 + tmp // 10

            if not visited[tmp]:
                visited[tmp] = True
                queue.append((tmp,record + act))
                
for _ in range(int(input())):
    init, goal = list(map(int,input().split()))
    print(BFS(init,goal))