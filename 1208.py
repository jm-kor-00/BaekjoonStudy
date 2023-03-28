import itertools
import bisect
import sys
input = sys.stdin.readline

#배열의 부분집합들의 합을 모두 구하여 오름차순 정렬된 리스트 형태로 반환하는 함수
def makeSubset(arr):
    result = []
    for i in range(1,len(arr) + 1):
        for el in itertools.combinations(arr,i):
            result.append(sum(el))
    return sorted(result)

#bisect를 활용하여 num이 arr안에 몇 개 있는 지 반환하는 함수 
def getMatchedNum(arr,num):
    left = bisect.bisect_left(arr,num)
    right = bisect.bisect_right(arr,num)
    return right - left

#입력의 개수와 찾아야 하는 수 입력
N, S = map(int,input().split())
arr = list(map(int,input().split()))

#입력받은 집합을 2개로 나눔
A_arr = arr[:N//2]
B_arr = arr[N//2:]

#A와 B의 부분집합들의 합을 구하여 정렬된 리스트로 만듬
Subset_A = makeSubset(A_arr)
Subset_B = makeSubset(B_arr)

#A안에서 S를 만들 수 있는 경우와 B안에서 S를 만들 수 있는 경우
count = getMatchedNum(Subset_A,S)
count += getMatchedNum(Subset_B,S)

#A와 B의 요소들을 함께 사용해서 S를 만들 수 있는 경우
for el in Subset_A:
    tmp = S - el
    count += getMatchedNum(Subset_B,tmp)

#결과출력
print(count)