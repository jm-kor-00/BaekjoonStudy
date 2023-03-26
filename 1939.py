import sys
input = sys.stdin.readline

N,M = map(int,input().split())
world = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    world[A][B].append(C)
S,E = map(int,input().split())
print(world)