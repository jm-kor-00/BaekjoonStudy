import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

left = 0
right = N - 1

lowest = float('inf')

while left < right:
    tmp = arr[left] + arr[right]
    if abs(tmp) < lowest :
        lowest = abs(tmp)
        result = arr[left],arr[right]
    if tmp > 0 : right -= 1
    elif tmp < 0 : left += 1
    else : break

print(result[0],result[1])