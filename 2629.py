import sys
input = sys.stdin.readline

n = int(input())
w_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

#배열 초기화, 초기값은 모두 False(불가능)
DP = [[False for _ in range(500 * n + 1)] for _ in range(n+1)]

# tmp = 몇번째 추에 대해서 계산하는지
# weight = 추를 넣냐 빼냐 안쓰냐에 따라 바뀌는 무게
def function(tmp,weight):
    #주어진 추의 개수를 넘어갔다면 #인덱스오류 방지
    if tmp > n :
        return
    #이미 계산했다면 #반복호출 방지
    if DP[tmp][weight]:
        return
    #가능으로 변경
    DP[tmp][weight] = True

    #다음 추로 넘어가며 3가지 경우에 대해 재귀호출

    #추 더하기
    function(tmp + 1, weight + w_list[tmp - 1])
    #추 빼기
    function(tmp + 1, abs(weight - w_list[tmp - 1])) #빼는 경우는 절댓값 처리
    #추 안쓰기
    function(tmp + 1, weight)

#main
function(0,0)
for m_weight in m_list:
    if m_weight > 500 * n:
        print("N",end=' ')
    else :
        if DP[n][m_weight]:
            print("Y",end=' ')
        else :
            print("N",end=' ')