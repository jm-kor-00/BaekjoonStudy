import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

DP = [0] * N
tmp = 0
DP[tmp] += nums[0]
MAX = DP[tmp]

for i in range(1,N):
    DP[tmp] += nums[i]
    MAX = max(MAX,DP[tmp],nums[i])
    if nums[i] < 0 :
        if DP[tmp] > 0 :
            pass
        else :
            tmp += 1
print(MAX)