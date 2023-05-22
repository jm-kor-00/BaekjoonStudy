#조합으로 생성되는 부분집합을 구할 수 있는 함수

from itertools import combinations
#return_list = list(combinations(list,r))
#nCr

arr = [1,2,3,4,5]
print(list(combinations(arr,3)))

#순열 부분집합 구할 수 있는 함수
from itertools import permutations
#return_list = list(combinations(list,r))
#nPr

#전단,말단 삽입/삭제가 가능한 파이썬 덱
from collections import deque
# queue = deque()

#제곱근함수
from math import sqrt
#실수로 출력됨
print(sqrt(26)) #5.099
#정수로 출력
print(round(sqrt(26)))
print(int(sqrt(26)))

arr = [1,2,3,4,10,9,8,7,6,5]
print("합 :", sum(arr))# 55
print("최소 :", min(arr))# 1
print("최대 :", max(arr))# 10
arr.sort()
print("정렬 후 :",arr)

STR = "1111"
# print(STR + 1)
# print(int(STR) + 1)

INT = 1111
# print(INT + "1")
print(str(INT) + "1")

#++++
if "11" in STR : print("True")