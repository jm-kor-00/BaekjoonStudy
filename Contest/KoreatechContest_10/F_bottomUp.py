import sys
sys = sys.stdin.readline

def DP(town:list):
    N = len(town)
    #메모지에이션 테이블
    #memo[i][j] : i번 집부터 j번 집을 가지고 진행할 때,
    #<마을이 얻을 수 있는 정신력 - 마왕이 얻은 정신력> 의 최대값
    memo = [[0 for _ in range(N)]for _ in range(N)]
    
    #i부터 i까지이면 town[i]가 최대값
    for i in range(N):
        memo[i][i] = town[i]

    #해당 반복문의 진행은
    #0,1 > 1,2 > .. > 0,2 > 1,3 > .. > 0,3 > 1,4 >
    for i in range(1,N):
        for s in range(N - i):
            e = s + i
            memo[s][e] = max(town[s] - memo[s+1][e],
                             town[e] - memo[s][e-1])
    
    # for row in memo :
    #     print(el)

    print(memo)

    #승리조건 : 마을의 정신력이 0 이상
    return memo[0][N-1] >= 0

for _ in range(int(input())):
    N = int(input())
    town = list(map(int,input().split()))

    print("One for all" if DP(town) else "All for one")