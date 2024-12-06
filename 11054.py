import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
rarr = arr[::-1]

inc=[1] * N; dec=[1] * N
for i in range(N):
    for j in range(i):
        #증가dp
        if arr[i] > arr[j]:
            inc[i] = max(inc[i],inc[j]+1)
        #감소dp, 여기서 i는 실제로는 N-1-i
        if rarr[i] > rarr[j]:
            dec[i] = max(dec[i],dec[j]+1)
ans = 0
for i in range(N):
    tmp = inc[i] + dec[N-1-i] - 1
    #수열 중간에 arr[i]를 기준으로 양쪽으로 증가 ~ i + i ~ 감소, arr[i]가 2번 세지므로 -1
    ans = max(tmp,ans)

print(ans)