import sys
import heapq
input = sys.stdin.readline

#딕셔너리로 정리한 시간집합{시간:증감}을
#최소힙을 활용하여 순차적으로 접근
def countServer(timeSet:dict):
    minH = []
    for key in timeSet:
        heapq.heappush(minH,(key, timeSet[key]))
    
    #이전 시간, 이전 증감
    prev_t, prev_s = heapq.heappop(minH)
    #사용중인 서버개수
    Server = prev_s

    #힙큐가 빌 때까지
    while minH:
        #현재 시간, 현재 증감
        tmp_t, tmp_s = heapq.heappop(minH)

        #출력 : 이전시간, 현재시간, 사용 개수
        print(prev_t,tmp_t,Server)

        #이전시간 초기화
        prev_t, prev_s = tmp_t, tmp_s
        #사용개수에 증감 적용
        Server += tmp_s

for _ in range(int(input())):
    timeSet = {}
    for _ in range(int(input())):
        F,L,S = map(int,input().split())
        
        if F in timeSet:
            timeSet[F] += S
        else : timeSet[F] = S
        
        if L in timeSet:
            timeSet[L] -= S
        else : timeSet[L] = -S

    countServer(timeSet)