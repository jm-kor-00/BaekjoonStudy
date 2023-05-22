import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input()) #숫자개수
arr = list(map(int,input().split())) #공백구분해서 정수 리스트 입력

nCr = list(combinations(arr,3)) #원소 3개씩 조합이 전부 들어가있다.
print(nCr)
count = 0 #0이되는 조합의 개수 count
for el in nCr :
    sum = 0
    for num in el:
        sum += num
    if sum == 0 : count += 1
print(count)