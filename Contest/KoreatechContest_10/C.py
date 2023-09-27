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
            used += works[idx]
            biggest = -1 * heapq.heappushpop(myOwn,-works[idx])
            used -= biggest
        else :
            biggest = works[idx]

        tmp = heapq.heappushpop(bootak,biggest)
        heapq.heappush(myOwn, -tmp)
        
        used += tmp
        if used > T :
            break
        idx += 1

    print(idx)