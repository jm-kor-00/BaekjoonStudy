import sys
input = sys.stdin.readline

#최소 dist만큼 떨어뜨리면서 설치할 수 있는 공유기의 수
def countAble(arr,dist,N):
    #현재 설치한 공유기 개수
    count = 1
    #설치한 곳 = 첫번째집
    cur = arr[0]
    for i in range(1,N):
        # cur로부터 dist 이상 떨어진 집을 찾으면
        if arr[i] >= cur + dist :
            count += 1
            #공유기 개수 증가 및 설치한 집 갱신
            cur = arr[i]
    return count

#적절한 거리를 찾기 위해 이분탐색
#매개변수 탐색으로 최소거리 출력
def binarySearch(arr,N,C):
    #가능한 범위 : 1 ~ (첫번쨰집부터 마지막 집까지 거리)
    left = 1
    right = arr[N - 1] - arr[0]

    #매개변수 탐색
    while left <= right:
        mid = (left + right) // 2
        count = countAble(arr,mid,N)
        #조건만족시
        if count >= C :
            #결과 갱신
            ans = mid
            #작은 쪽 갱신
            left = mid + 1
        else :
            #큰 쪽 갱신
            right = mid - 1
    return ans

#집의 수와 공유기의 수 입력
N, C = map(int,input().split())
house = []

#각 집의 좌표 입력
for i in range(N):
    house.append(int(input()))
#오름차순 정렬
house.sort()

#함수 실행 및 출력
print(binarySearch(house,N,C))