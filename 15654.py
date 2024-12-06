import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

tmp = []
def recu():
    global tmp,arr,N,M
    if len(tmp) == M:
        print(' '.join(map(str,tmp)))
        return
    for i in range(N):
        if arr[i] != 0:
            t = arr[i]; tmp.append(arr[i])
            arr[i] = 0
            recu()
            arr[i] = t; tmp.pop()
recu()