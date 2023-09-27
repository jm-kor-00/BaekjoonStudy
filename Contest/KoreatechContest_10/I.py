import sys
input = sys.stdin.readline

def countP(wait, time):
    P = 0
    for el in wait:
        P += time // el

    return P

def BinarySearch(S,wait,low,high):
    while low <= high :
        mid = (low + high) // 2
        tmp = countP(wait, mid)

        if tmp < S :
            low = mid + 1
        elif tmp >= S :
            ans = mid
            high = mid - 1

    return ans

for _ in range(int(input())):
    S, C = map(int,input().split())
    wait = list(map(int,input().split()))
    
    low = 0
    high = max(wait) * S

    print(BinarySearch(S, wait, low, high))