import sys
from collections import deque
input = sys.stdin.readline

def convert(num):
    arr = [0,0,0,0]
    for i in range(3,-1,-1):
        arr[3 - i] = num // (10 ** i)
        num -= arr[3-i] * (10**i)
    return arr

def toInt(arr):
    num = 0
    for i in range(4):
        num += arr[i] * (10**(3 - i))
    return num

def BFS(init,goal):
    queue = deque()
    visited = [[[["" for _ in range(10)]for _ in range(10)] for _ in range(10)]for _ in range(10)]
    queue.append(init)
    while queue :
        #큐에 있는 리스트 pop
        tmp = queue.popleft()
        print(tmp)
        #변경기록 반환
        record = visited[tmp[0]][tmp[1]][tmp[2]][tmp[3]]
        if tmp == goal : return record

        for i in range(4):
            if i == 0: #D
                num = toInt(tmp) #정수로 변경
                num = (2 * num) % 10000 #D 연산 수행
                chg = convert(num)
                tmpAct = "D"
            elif i == 1: #S
                num = toInt(tmp) #정수로 변경
                num -= 1 #1감소
                if num < 0:
                    chg = [9,9,9,9]
                else : chg = convert(num)
                tmpAct = "S"
            elif i == 2: #L
                chg = [tmp[1],tmp[2],tmp[3],tmp[0]]
                tmpAct = "L"
            else : #R
                chg = [tmp[3],tmp[0],tmp[1],tmp[2]]
                tmpAct = "R"

            if not len(visited[chg[0]][chg[1]][chg[2]][chg[3]]) < len(record) :
                visited[chg[0]][chg[1]][chg[2]][chg[3]] += tmpAct
                queue.append(chg)
                print(tmp,chg)

for _ in range(int(input())):
    n1, n2 = list(map(int,input().split()))
    init = convert(n1)
    goal = convert(n2)
    record = BFS(init,goal)
    print(record)