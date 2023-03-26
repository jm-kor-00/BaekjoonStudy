import sys
input = sys.stdin.readline
N, M = map(int,input().split())
Trees = list(map(int,input().split()))

left = 0
right = 1000000000

def checkTrees(mid,Trees):
    total = 0
    for el in Trees:
        tmp = el - mid
        if tmp > 0 :
            total += tmp
    return total

while left <= right :
    mid = (left + right) // 2
    tmp = checkTrees(mid,Trees)
    
    if tmp >= M :
        ans = mid
        left = mid + 1
    else :
        right = mid - 1

print(ans)