from copy import deepcopy
import random

def make_arr(n):
    arr = []
    zero = 0; one = 0
    while zero < n // 2 and one < n // 2:
        tmp = random.randrange(0,2)
        arr.append(tmp)
        if tmp == 0: zero += 1
        else : one += 1
    for i in range(zero,n // 2):
        arr.append(0)        
    for i in range(one,n // 2):
        arr.append(1)
    return arr      

def bubble_sort(arr):
    total = 0
    print("정렬전 :",arr)
    #버블정렬과정
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            total += 1 #비교연산 1
            #앞의 요소가 뒤의 요소보다 크면
            if arr[j] > arr[j+1]:
                #두 요소의 자리 교체
                arr[j],arr[j+1] = arr[j+1],arr[j]
                total += 2 #대입연산 2
        print(i+1,"Step :",arr) #정렬과정 출력
    print("결과 :",arr)
    print("연산 횟수 :",total)

def my_sorting1(arr):
    total = 0
    print("정렬전 :",arr)
    # arr의 앞부분(0부터 len(arr) / 2 까지)을 확인
    for i in range(len(arr) // 2):
        total += 1 #비교연산 +1
        # 1이 리스트의 앞부분에 있으면
        if arr[i] == 1:
            # arr의 뒷부분(len(arr)/2 부터 len(arr) - 1까지)을 확인
            for j in range(len(arr)//2, len(arr)):
                total += 1 #비교연산 +1
                # 0이 리스트의 뒷부분에 있으면
                if arr[j] == 0:
                    #arr[i]와 arr[j]의 값을 교환
                    arr[j],arr[i] = arr[i],arr[j]
                    total += 2 #대입연산 2
                    break
        print(i+1,"Step :",arr) #정렬과정 출력
    print("결과 :",arr)
    print("연산 횟수 :",total)

def my_sorting2(arr):
    total = 0
    print("정렬전 :",arr)
    for i in range(len(arr) // 2):
        for j in range(len(arr) // 2):
            total += 1 #비교연산
            if arr[j] == 1:
                total += 2 #삭제, 삽입연산
                arr.pop(j)
                arr.append(1)
        print(i+1,"Step :",arr) #정렬과정 출력
    print("결과 :",arr)
    print("연산 횟수 :",total)

#main
if __name__ == "__main__":
    arr1 = make_arr(12)
    arr2 = deepcopy(arr1)
    arr3 = deepcopy(arr1)
    print("***문제 설명에 나온 해결방법***\n")
    bubble_sort(arr1)
    print("====================================")
    print("***내가 개선한 해결방법1***\n")
    my_sorting1(arr2)
    print("====================================")
    print("***내가 개선한 해결방법2***\n")
    my_sorting2(arr3)