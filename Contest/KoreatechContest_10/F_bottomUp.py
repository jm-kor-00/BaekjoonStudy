import sys
sys = sys.stdin.readline

def DP(town:list):
    N = len(town)
    memo = [[0 for _ in range(N)]for _ in range(N)]
    
    for i in range(N):
        memo[i][i] = town[i]

    for i in range(1,N):
        for s in range(N - i):
            e = s + i
            memo[s][e] = max(town[s] - memo[s+1][e],
                             town[e] - memo[s][e-1])
    
    # for row in memo :
    #     print(el)
    return memo[0][N-1] >= 0

for _ in range(int(input())):
    N = int(input())
    town = list(map(int,input().split()))

    print("One for all" if DP(town) else "All for one")