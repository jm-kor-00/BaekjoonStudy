import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
tmp = []
visited = [False] * N
def recu(count):
    global N,M
    if count == M :
        print(*tmp); return
    before = 0
    for n in range(N):
        if visited[n] or before == arr[n] : continue
        tmp.append(arr[n]); visited[n] = True
        before = arr[n]
        recu(count+1)
        tmp.pop(); visited[n] = False
        
recu(0)