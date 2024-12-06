import sys
import heapq
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

def findSharedNum(a,b):
    c = [-a[x] for x in range(len(a))]; heapq.heapify(c)
    for i in range(len(a)):
        tmp = heapq.heappop(c) * -1
        for j in range(len(b)):
            if b[j] == tmp:
                for k in range(len(a)):
                    if tmp == a[k]:
                        return [k, j, tmp]
    return False

tmpA = A; tmpB = B
Ans = []

while True:
    t = findSharedNum(tmpA,tmpB)
    if not t : break
    Ans.append(t[2])
    if t[0]+1 == len(tmpA) or t[1]+1 == len(tmpB):
        break
    tmpA = list(tmpA[t[0]+1:])
    tmpB = list(tmpB[t[1]+1:])

print(len(Ans))
if len(Ans) > 0:
    for el in Ans:
        print(el,end=' ')