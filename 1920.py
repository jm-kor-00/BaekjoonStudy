import sys
input = sys.stdin.readline

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
        
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

T = int(input())
test = list(map(int,input().split()))

for el in test:
    if binarySearch(arr,el):
        print("1")
    else :
        print("0")