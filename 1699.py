N = int(input())
DP = [0] * (N + 1)
tmp_mod = 0

for i in range(1,N + 1):
    if i == (tmp_mod + 1) ** 2:
        DP[i] = 1
        tmp_mod += 1
    else :
        DP[i] = DP[i - 1] + 1
        for j in range(tmp_mod,1,-1):
            if DP[i] - 1 > DP[i - j ** 2]:
                DP[i] = DP[i - j ** 2] + 1
print(DP[N])