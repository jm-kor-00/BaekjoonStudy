import sys
from collections import deque
input = sys.stdin.readline

def checking(PQ,target):
    count = 1
    while(PQ):
        tmp = PQ.popleft()
        _pop = True
        for el in PQ:
            if el[0] > tmp[0] :
                PQ.append(tmp)
                _pop = False
                break
        if _pop:
            if tmp[1] == target:
                return count
            else : count += 1
    return count
            
for _ in range(int(input())):
    N, target = map(int,input().split())
    arr = list(map(int,input().split()))
    PQ = deque()
    for i in range(N):
        PQ.append([arr[i],i])
    print(checking(PQ,target))