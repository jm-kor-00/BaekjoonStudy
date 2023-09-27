import sys
sys = sys.stdin.readline

def DP(town:list,memo:list,s:int,e:int):
    if s == e:
        return town[s]
    
    if memo[s][e] != None:
        return memo[s][e]
     
    else :
        memo[s][e] = max(town[e] - DP(town,memo,s,e-1),
                         town[s] - DP(town,memo,s+1,e))
        
        return memo[s][e]

for _ in range(int(input())):
    N = int(input())
    town = list(map(int,input().split()))
    
    memo = [[None for _ in range(N)]for _ in range(N)]

    res = DP(town,memo,0,N-1) >= 0
    print("One for all" if res else "All for one")