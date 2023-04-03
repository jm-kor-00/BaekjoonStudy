import random
#1,2,...,N 인 배열에서 임의로 하나를 제거하는 함수
def random_Exception(N):
    arr = [i for i in range(1,N+1)]
    ex = random.randrange(1,N+1)
    
    arr.remove(ex)

    print("무작위로 제외된 숫자 : ",ex)
    print("배열 :",arr)
    return arr

#이진탐색을 활용한 매개변수탐색으로
#제외된 숫자를 찾는 함수

def findExcpetion(arr):
    left = 0
    right = len(arr) - 1
    ans = len(arr)
    #이진탐색
    while left <= right :
        mid = (left + right) // 2
        #조건 : mid번째 숫자가 mid + 1이 아니면
        # 0번 ~ mid번 인덱스 사이에 빈 곳이 있음
        if arr[mid] != mid + 1 :
            ans = mid #정답갱신
            right = mid - 1 #큰 쪽 갱신
        else :
            left = mid + 1#작은 쪽 갱신
        print(left,right,mid)
    return ans + 1
#main
N = int(input('배열의 크기 :'))
arr = random_Exception(N) #크기가 N-1인 빈 숫자있는 배열 생성
print("탐색 결과 : ",findExcpetion(arr))