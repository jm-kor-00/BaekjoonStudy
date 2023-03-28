# N x N배열에서 mid보다 작은 수의 개수를 반환하는 함수
def find_less(N,mid):
    count = 0
    for i in range(1,N + 1):
        tmp = mid // i
        # N보다 크다면 tmp를 N으로 수정해야 함
        if tmp > N : tmp = N
        count += tmp #tmp를 count에 더함
    return count

N = int(input())
K = int(input())

#가능한 수의 범위는 1부터 N의 제곱
left = 1
right = N ** 2

#이분탐색
while left <= right:
    mid = (left + right) // 2
    tmp = find_less(N,mid)
    
    #right를 수정하기 때문에 mid는 작아짐
    #별도의 탈출문없이 계속해서 반복문이 돌아가게 되면
    #mid는 조건을 만족하는 가장 작은 수로 맞춰지게 됨
    if tmp >= K :
        #결과갱신
        ans = mid
        right = mid - 1
    else :
        left = mid + 1

print(ans)