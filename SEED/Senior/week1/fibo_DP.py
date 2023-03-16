N = int(input())
# 1. 배열을 하나 만들기
DP = [0] * (N + 1)
# 2. 초기값 넣기
DP[0] = 0
DP[1] = 1
# 3. 답을 구할 때까지 반복!
for i in range(2,N + 1):
    if DP[i] : continue
    else : DP[i] = DP[i - 1] + DP[i - 2]
# 4. 결과출력
print(DP[N])