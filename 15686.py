import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
town = []
for _ in range(N):
    town.append(list(map(int,input().split())))

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            house.append((i,j))
        elif town[i][j] == 2:
            chicken.append((i,j))

def chi_dis(chs,house):
    total = 0
    for h in house:
        dis = 100
        hx,hy = h
        for c in chs:
            cx,cy = c
            tmp = abs(hy-cy) + abs(hx-cx)
            dis = min(tmp,dis)
        total += dis
    return total

MIN = float('INF')
SET = set(chicken)

def recur(pos,cnt):
    global MIN, SET, M, chicken
    if cnt == M:
        MIN = min(chi_dis(SET,house),MIN)
        return
    if cnt - (len(chicken) - pos + 1) > M or pos >= len(chicken):
        return
    if cnt > 0 :
        if chi_dis(SET,house) > MIN :
            return
    SET.remove(chicken[pos])
    recur(pos+1,cnt-1)
    SET.add(chicken[pos])
    recur(pos+1,cnt)

recur(0,len(chicken))
print(MIN)