#수열도 구하는
#이분탐색 LIS 문제
import bisect
import sys
from collections import deque as DQ
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

#-10억까지 가능하므로 첫 항은 음의 무한대
LIS = [float("-inf")]
#삽입 기록을 나타낼 덱 (스택으로 사용)
record = DQ()
#추적하여 LIS의 요소들을 저장할 덱 (스택으로 사용)
result = DQ()

for el in arr:
    #현재 마지막 요소보다 크면
    if LIS[-1] < el:
        #기록에 저장
        record.append((el,len(LIS)))
        #LIS에 삽입
        LIS.append(el)
    else :
        #이분탐색으로 LIS에서 적합한 위치를 idx에 저장
        idx = bisect.bisect_left(LIS,el)
        #LIS[idx]를 갱신
        LIS[idx] = el
        #기록에 저장
        record.append((el,idx))
#최장 부분 수열의 길이는 LIS의 길이 - 1 , 초기에 음의 무한대 수를 하나 넣었었기 때문
count = len(LIS) - 1
print(count)

#record의 꼬리부터 역으로 탐색
while count != 0:
    tmp_item, tmp_idx = record.pop()
    if tmp_idx == count:
        result.append(tmp_item)
        count -= 1
#현재 result에는 역으로 들어가 있기 때문에 
while result :
    print(result.pop(),end=' ')