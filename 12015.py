#길이만 구하는
#이분탐색 LIS 문제
import bisect
import sys
input = sys.stdin.readline

#크기, 수열 입력
N = int(input())
arr = list(map(int,input().split()))

LIS = [arr[0]]

for el in arr:
    #LIS의 마지막 요소보다 배열의 요소가 크면
    if LIS[-1] < el:
        #LIS에 말단 삽입
        LIS.append(el)
    #???
    else :
        #이분탐색으로 el이 적합한 위치를 탐색해서 인덱스 반환
        idx = bisect.bisect_left(LIS,el)
        #탐색한 자리에 삽입
        LIS[idx] = el

print(len(LIS))