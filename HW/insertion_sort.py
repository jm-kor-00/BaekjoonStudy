from copy import deepcopy
import random

#Bottom-UP방식 삽입정렬 알고리즘
def insertion_sort_BottomUP(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        #key의 올바른 자리를 찾는 과정
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
        #step별 상태 출력
        print("step %d:"%(i),arr)
    return arr

#topdowm방식으로 구현할 때 key를 올바른 자리에 넣는 과정을 함수화함
def insertion(key,arr):
    for i in range(len(arr)):
        #key를 제외한 arr는 이미 오름차순 정렬이 끝나있으므로
        #key보다 큰 값을 찾으면 그 자리에 key를 넣으면 완료
        if key < arr[i]:
            arr.insert(i,key)
            #step출력용
            print("step %d:"%(len(arr)),arr)
            return arr
    #arr의 모든 요소가 key보다 작으면
    #리스트 맨 뒤에 추가
    arr.append(key)
    #step출력
    print("step %d:"%(len(arr)),arr)
    return arr
#재귀호출로 삽입정렬을 수행하는 함수
def insertion_Sort_TopDown(arr):
    if len(arr) == 0:
        return []
    else :
        #key와 리스트의 나머지를 분리하여 또다시 재귀호출
        return insertion(arr[0],insertion_Sort_TopDown(arr[1:]))
#main
if __name__ == "__main__":
    n = (int(input("배열크기 : ")))
    arr1 = [i for i in range(1,n+1)]
    
    random.shuffle(arr1)
    arr2 = deepcopy(arr1)
    
    print("+++++++++++++++++++++++++++++++++++++++")
    print("[Bottom-Up 삽입정렬]\n")
    print("정렬 전 :",arr1)
    print()
    sortedArr1 = insertion_sort_BottomUP(arr1)
    print("\n정렬결과 :",sortedArr1)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("[Top-Down 삽입정렬]\n")
    print("정렬 전 :",arr2)
    print()
    sortedArr2 = insertion_Sort_TopDown(arr2)
    print("\n정렬결과 :",sortedArr2)
    print("+++++++++++++++++++++++++++++++++++++++")