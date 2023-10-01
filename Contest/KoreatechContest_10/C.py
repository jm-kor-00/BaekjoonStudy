import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    T, B, W = map(int,input().split())
    works = list(map(int,input().split()))
    
    #부탁횟수가 외주 개수보다 많으면
    if B >= W :
        print(W)
        continue
    
    bootak = [] #맡길 일
    myOwn = [] #직접할 일

    used = 0 #직접 일한 시간
    idx = B #현재pos

    #일단 다 부탁함
    for i in range(B):
        heapq.heappush(bootak, works[i])

    while idx < W :
        #직접한 일이 있으면
        if myOwn :
            used += works[idx]
            
            #최대힙 사용법을 유의
            #직접한 일 중에 가장 오래 걸리는 일을 빼냄
            biggest = -1 * heapq.heappushpop(myOwn,-works[idx])
            used -= biggest

        #아직 직접한 일이 없을 때
        else :
            biggest = works[idx]

        #위에 biggest를 부탁에 포함해서 가장 짧은 일을 찾아냄
        tmp = heapq.heappushpop(bootak,biggest)

        #가장 짧은 일은 직접 함 -> myOwn에 삽입, 사용 시간에 추가
        heapq.heappush(myOwn, -tmp)
        used += tmp

        #시간을 다 쓰면 종료
        if used > T :
            break
        idx += 1

    print(idx)