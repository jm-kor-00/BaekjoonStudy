import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

DP = [[0 for _ in range(N)] for _ in range(2)]
DP[0][0] = arr[0]
# 첫값을 넣지 않고 나온 연속합은 포함되지 않게 처리
DP[1][0] = -float("inf")

for i in range(1, N):
    # 제거하지 않는 경우의 최대 연속합
    DP[0][i] = max(DP[0][i - 1] + arr[i], arr[i])
    # 제거하는 경우의 최대 연속 합
    DP[1][i] = max(DP[0][i - 1], DP[1][i - 1] + arr[i])

# 둘 중 큰 값이 정답
print(max(max(DP[0]), max(DP[1])))
