import sys
input = sys.stdin.readline

Arr = list(map(int,input().strip()))
N = len(Arr)

DP = [0] * N

#첫자리
if Arr[0] > 0 : 
    DP[0] += 1
#두번째 자리
if N == 1:
    print(DP[0] % 1000000)
else :
    if Arr[1] > 0 :
        DP[1] = 1
    if 10 <= Arr[0] * 10 + Arr[1] <= 26 : 
        DP[1] += 1
        
    if Arr[0] * 10 + Arr[1] <= 9 :
        DP[1] = 0
    else :
        for i in range(2,N):
            if Arr[i] > 0 :
                DP[i] = DP[i - 1]
                
            if 10 <= Arr[i - 1] * 10 + Arr[i] <= 26 :
                DP[i] += DP[i - 2]
    print(DP[N-1] % 1000000)