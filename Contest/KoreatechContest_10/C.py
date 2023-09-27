import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    T, B, W = map(int,input().split())
    works = list(map(int,input().split()))
    
    if B >= W :
        print(W)
        continue

    bootak = []
    myOwn = []

    used = 0
    idx = B

    for i in range(B):
        heapq.heappush(bootak, works[i])

    while idx < W :
        if myOwn :
            tmp = -1 * heapq.heappushpop(myOwn,-works[idx])
            used -= tmp
        else :
            tmp = works[idx]
        cmp = heapq.heappushpop(bootak,tmp)
        heapq.heappush(myOwn, cmp)
        used += cmp
        if used > T :
            break
        idx += 1

    print(idx - 1)