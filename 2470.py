import sys
import bisect as BS
input = sys.stdin.readline


N = int(input())
arr = list(map(int,input().split()))
arr.sort()

result_set = (-float('inf'),float('inf'))
lowest = float('inf')

pos = BS.bisect_left(arr,0)



for i in range(pos + 1):
    partner = BS.bisect_left(arr[i+1:-1],-arr[i])
    tmp_sum = abs(arr[partner] + arr[i])
    if tmp_sum == 0:
        result_set = (arr[i],arr[partner])
        break
    #0은 아니지만 최소값 갱신 상황
    elif tmp_sum < lowest:
        result_set = (arr[i],arr[partner])
        lowest = tmp_sum

print(min(result_set),max(result_set))