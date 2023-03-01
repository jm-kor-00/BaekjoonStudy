import sys
input = sys.stdin.readline

N, K = map(int,input().split())
#물건들 스케줄
scd = list(map(int,input().split()))
mulTap = [] #멀티탭
result = 0 #뽑은 횟수 = 결과

for i in range(K):
    #이미 꽂혀있다면
    if scd[i] in mulTap : continue
    #빈자리가 있다면
    if len(mulTap) < N :
        mulTap.append(scd[i])
        continue
    #가장 뒤에 사용할 물건의 인덱스
    latest = 0
    #꽂혀있는 물건들중에
    for el in mulTap:
        #나중에 사용하지 않을 물건이 있다면
        if el not in scd[i:]:
            #뽑을대상으로 지정, for문 탈출
            tmp = el; break
        #가장 뒤에 사용할 물건 찾는 과정
        elif scd[i:].index(el) > latest:
            #가장 뒤에 사용할 물건의 인덱스 최신화
            latest = scd[i:].index(el)
            #뽑을 대상으로 지정
            tmp = el
    #뽑기로 결정된 물건의 자리를 현재 꽂아야할 물건으로 대체
    mulTap[mulTap.index(tmp)] = scd[i]
    #결과 횟수 + 1
    result += 1
print(result)