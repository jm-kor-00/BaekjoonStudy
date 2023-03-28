import sys
import bisect as BS
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

T = int(input())
test = list(map(int,input().split()))

for el in test:
    #bisect_right의 결과에서
    #bisect_left를 빼내면
    #리스트에 존재하는 el의 개수를 얻을 수 있음 
    left = BS.bisect_left(arr,el)
    right = BS.bisect_right(arr,el)
    print(right-left,end=' ')