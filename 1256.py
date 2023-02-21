N,M,K = map(int,input().split())

#DP는 DP[0][0] ~ DP[N][M]까지 1로 초기화
DP = [[1 for _ in range(M+1)] for _ in range(N+1)]
#결과저장용 변수
result = ""
#점화식
for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]

if DP[N][M] < K :
    result = -1
else :
    while N > 0 and M > 0 :
        tmp = DP[N-1][M]
        if K <= tmp:
            N -= 1
            result += 'a'
        else :
            M -= 1
            result += 'z'
            K -= tmp
    if N > 0 or M > 0:
        result += 'a' * N + 'z' * M
print(result)