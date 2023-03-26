import sys
import bisect as BS
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

T = int(input())
test = list(map(int,input().split()))

for el in test:
    left = BS.bisect_left(arr,el)
    right = BS.bisect_right(arr,el)
    print(right-left,end=' ')