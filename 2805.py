import sys
input = sys.stdin.readline

#나무의 수, 필요한 나무 길이 입력
N, M = map(int,input().split())
#각 나무의 길이를 입력받음
Trees = list(map(int,input().split()))

#문제 조건에 따라 가능한 범위 : 0이상 10억이하
left = 0
right = 1000000000

#mid로 잘랐을 때 얻는 나무의 길이를 반환하는 함수
def checkTrees(mid,Trees):
    total = 0
    for el in Trees:
        tmp = el - mid
        #잘라내는 길이가 나무보다 크면 얻는 것은 0이므로
        #양수가 아닌 경우는 제외
        if tmp > 0 :
            total += tmp
    return total

#매개변수 탐색으로 최소 길이를 찾음
while left <= right :
    mid = (left + right) // 2
    #현재 길이 : mid 로 나무들을 자를때 얻는 나무길이를 저장
    tmp = checkTrees(mid,Trees)
    
    #필요한 길이보다 길거나 같으면
    if tmp >= M :
        #결과 갱신
        ans = mid
        #좌측끝 갱신 => 얻는 나무길이 감소
        left = mid + 1
    else : #나무를 더 잘라야 함
        #우측끝 갱신
        right = mid - 1

print(ans)