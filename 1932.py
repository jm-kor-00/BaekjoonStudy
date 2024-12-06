import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    tri = []
    for _ in range(N):
        tri.append(list(map(int,input().split())))
    
    if N == 1:
        return tri[0][0]
    
    DP = [[0 for _ in range(N+1)]for i in range(N)]
    
    DP[0][0] = tri[0][0]
    DP[1][0] = DP[0][0] + tri[1][0]
    DP[1][1] = DP[0][0] + tri[1][1]
    for i in range(2,N):
        DP[i][0] = tri[i][0] + DP[i-1][0]
        DP[i][i] = tri[i][i] + DP[i-1][i-1]
        for j in range(i):
            DP[i][j] = tri[i][j] + max(DP[i-1][j-1],DP[i-1][j])
    return max(DP[N-1])
print(solution())