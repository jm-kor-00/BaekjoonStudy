import sys
input = sys.stdin.readline
glass = []
sum = 0
#main
N = int(input())
for i in range(N):
    glass.append(int(input()))

if N <= 2 :
    for el in glass :
        sum += el
else :
    case0 = [0 for i in range(N)]
    case1 = [0 for i in range(N)]
    case2 = [0 for i in range(N)]
    
    case0[1] += glass[0]
    case1[1] += glass[1]
    case2[1] += glass[0] + glass[1]

    for i in range(2,N):
        case0[i] += max(case0[i-1],case1[i-1],case2[i-1])
        case1[i] += (case0[i-1] + glass[i])
        case2[i] += (case1[i-1] + glass[i])
    sum = max(case0[N - 1],case1[N - 1],case2[N - 1])

print(sum)