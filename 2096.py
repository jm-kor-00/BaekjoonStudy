import sys
input = sys.stdin.readline

N = int(input())
maxDP = list(map(int,input().split()))
minDP = [maxDP[0],maxDP[1],maxDP[2]]

for _ in range(1,N):
    tmp = list(map(int,input().split()))
    a = max(maxDP[0],maxDP[1]) + tmp[0]
    b = max(maxDP[0],maxDP[1],maxDP[2]) + tmp[1]  
    c = max(maxDP[1],maxDP[2]) + tmp[2]

    d = min(minDP[0],minDP[1]) + tmp[0]  
    e = min(minDP[0],minDP[1],minDP[2]) + tmp[1]  
    f = min(minDP[1],minDP[2]) + tmp[2]

    maxDP = [a,b,c]
    minDP = [d,e,f]

print(max(maxDP),min(minDP))