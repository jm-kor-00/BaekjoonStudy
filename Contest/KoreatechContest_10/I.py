import sys
input = sys.stdin.readline

def countP(wait, time):
    P = 0
    for el in wait:
        P += time // el
    #주어진 시간으로 처리할 수 있는 최대 인원수
    return P

#특정함수를 사용하여 탐색조건의 변경하며 진행하는 이진탐색
#백준 : 매개변수 탐색

def BinarySearch(S,wait,low,high):
    #중요*******
    while low <= high :
        mid = (low + high) // 2
        tmp = countP(wait, mid)
        
        #********************
        #low 혹은 high, 어느 쪽에서 ans를 초기화할 것인지
        #어느쪽의 등호를 열어놓을 것인지
        if tmp < S :
            low = mid + 1
        elif tmp >= S :
            ans = mid
            high = mid - 1

    return ans

for _ in range(int(input())):
    S, C = map(int,input().split())
    wait = list(map(int,input().split()))
    
    low = 0 #초기값 : 0
    high = max(wait) * S
    # 최대값 : 가장 오래 걸리는 코너로 모든 학생 처리하는 시간

    print(BinarySearch(S, wait, low, high))