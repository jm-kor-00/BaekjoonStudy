import sys
input = sys.stdin.readline

#이분탐색으로 리스트에  num이 있는 지 반환하는 함수
def binarySearch(arr,num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > num :
            right = mid - 1
        elif arr[mid] < num :
            left = mid + 1
        else : return True
    return False

#수의 개수 입력
N = int(input())
#리스트 입력받음
arr = list(map(int,input().split()))
#리스트 정렬
arr.sort()

#테스트 개수
T = int(input())
#테스트할 숫자들 입력
test = list(map(int,input().split()))

for el in test:
    #있으면 1, 없으면 0 출력
    if binarySearch(arr,el):
        print("1")
    else :
        print("0")