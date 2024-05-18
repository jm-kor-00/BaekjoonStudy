from collections import deque
import sys
input = sys.stdin.readline

def isIn(N,x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def turn(tD, fD):
    if fD == 'L':
        if tD[0] == 0:
            return (-tD[1], tD[0])
        else :
            return (tD[1],tD[0])

    else :
        if tD == 0:
            return (tD[1],tD[0])
        else :
            return (tD[1],-tD[0])

def solution():
    N = int(input())
    board = [[0 for _ in range(N)]for _ in range(N)]
    for _ in range(int(input())):
        x,y = map(int,input().split())
        board[x-1][y-1] = 1

    que = deque()
    for _ in range(int(input())):
        L = list(input().split()) #전환시점, 방향
        que.append((int(L[0]),L[1]))

    tD = (0,1) #현재 방향 = 오른쪽
    Body = deque() #뱀 몸체
    Body.append((0,0)) #머리 초기좌표 , 현재 길이 : 1
    cnt = 0 #턴 진행 횟수
    while True:
        if que:
            tT, fD = que.popleft()
            fD = turn(tD,fD)
        else :
            tT = cnt + N
        for _ in range(tT - cnt): #방향이 바뀔때까지 진행함
            cnt += 1
            tHx,tHy = Body.popleft()
            Body.appendleft((tHx,tHy))
            tHx += tD[0]; tHy += tD[1]
            
            if not isIn(N,tHx,tHy): return cnt #맵밖에 머리박음
            for el in Body: #몸이랑 겹치는 지 확인
                if el[0] == tHx and el[1] == tHy:
                    return cnt
                
            Body.appendleft((tHx,tHy)) #머리증가

            if board[tHx][tHy] == 1: #사과먹음
                board[tHx][tHy] = 0
            else : #사과없음
                Body.pop() #꼬리자르기

        tD = fD #방향전환

print(solution())