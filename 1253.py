import sys

def isGood(N,S,arr):
    left = 0
    right = N - 2
    while left < right:
        tmp = arr[left] + arr[right]
        if tmp > S : right -= 1
        elif tmp < S : left += 1
        else : return True
    return False

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
GOOD = 0

for i in range(N - 1):
    tmp_arr = arr[:i] + arr[i + 1:]
    # print(arr[i],tmp_arr)
    if isGood(N,arr[i],tmp_arr):
        GOOD += 1
# N-1번째만 따로, 배열만들기 방법이 달라서
tmp_arr = arr[:N-1]
if isGood(N,arr[N-1],tmp_arr):
    GOOD += 1

print(GOOD)