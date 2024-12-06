import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

DP=[[0 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1] :
            DP[i][j] = DP[i-1][j-1] + 1
        else :
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])

print(DP[len(s1)][len(s2)])