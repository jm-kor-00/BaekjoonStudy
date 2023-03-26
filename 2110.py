import sys
input = sys.stdin.readline

def countAble(arr,dist,N):
    count = 1
    cur = arr[0]
    for i in range(1,N):
        if arr[i] >= cur + dist :
            count += 1
            cur = arr[i]
    return count

def binarySearch(arr,N,C):
    left = 1
    right = arr[N - 1] - arr[0]

    while left <= right:
        mid = (left + right) // 2
        count = countAble(arr,mid,N)
        if count >= C :
            ans = mid
            left = mid + 1
        else :
            right = mid - 1
    return ans

N, C = map(int,input().split())
house = []

for i in range(N):
    house.append(int(input()))
house.sort()

print(binarySearch(house,N,C))