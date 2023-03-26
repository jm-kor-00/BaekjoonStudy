import itertools
import bisect
import sys
input = sys.stdin.readline

def makeSubset(arr):
    result = []
    for i in range(1,len(arr) + 1):
        for el in itertools.combinations(arr,i):
            result.append(sum(el))
    return sorted(result)

def getMatchedNum(arr,num):
    left = bisect.bisect_left(arr,num)
    right = bisect.bisect_right(arr,num)
    return right - left

N, S = map(int,input().split())
arr = list(map(int,input().split()))

A_arr = arr[:N//2]
B_arr = arr[N//2:]

Subset_A = makeSubset(A_arr)
Subset_B = makeSubset(B_arr)

count = getMatchedNum(Subset_A,S)
count += getMatchedNum(Subset_B,S)

for el in Subset_A:
    tmp = S - el
    count += getMatchedNum(Subset_B,tmp)

print(count)