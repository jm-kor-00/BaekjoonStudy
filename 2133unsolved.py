import sys
input = sys.stdin.readline

N = int(input())

DP = [0] * (N + 1)


DP[1] = 0
DP[2] = 3
for i in range(3,N + 1):
    