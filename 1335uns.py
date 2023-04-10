from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]
B, S = map(int,input().split())

cake = [[1 for _ in range(B*2)]for _ in range(B*2)]

for i in range(B - S, B + S):
    for j in range(B - S, B + S):
        cake[i][j] = 0

for el in cake:
    print(el)

def BFS(S):
    