N,M,K = map(int,input().split())

#결과저장용 변수
result = ""
#DP는 DP[0][0] ~ DP[N][M]까지 1로 초기화
DP = [[1 for _ in range(M+1)] for _ in range(N+1)]
#점화식
for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]
#만들 수 있는 문자열의 수를 초과하는 경우
if DP[N][M] < K :
    result = -1
else :
    while N > 0 and M > 0 :
        #첫자리가 a인 문자열의 개수
        tmp = DP[N-1][M]
        #작거나 같으면
        if K <= tmp:
            #첫자리가 'a'인 것.
            #'a'로 확정하고 N -= 1
            N -= 1
            result += 'a'
        else :
            #첫자리가 'z'인 것.
            #'a'로 확정하고 M -= 1
            #첫 자리가 'a'인 문자열의 수만큼 K 감소
            M -= 1
            result += 'z'
            K -= tmp
    #남은 a,z를 추가해줌
    result += 'a' * N + 'z' * M
#결과출력
print(result)