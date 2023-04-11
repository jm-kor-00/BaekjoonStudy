import sys
input = sys.stdin.readline
#main
N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))

if N <= 2:
    sum = 0
    for el in stairs:
        sum += el
    print(sum)
else :
    DP = [0 for i in range(N)]
    DP[0] = stairs[0]
    DP[1] = stairs[0] + stairs[1]
    DP[2] = max((stairs[0]+stairs[2]),(stairs[1]+ stairs[2])) 
    for i in range(3,N):
        DP[i] = max((DP[i - 2] + stairs[i]),(DP[i - 3] + stairs[i - 1] + stairs[i]))
    print(DP[N - 1])