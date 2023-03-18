import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coin = []
total = 0

for _ in range(N):
    coin.append(int(input()))

while K != 0:
    tmp = K // coin[N-1]
    total += tmp
    K -= coin[N-1] * tmp
    N -= 1
print(total)