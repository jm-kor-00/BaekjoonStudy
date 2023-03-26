def find_less(N,mid):
    count = 0
    for i in range(1,N + 1):
        tmp = mid // i
        if tmp > N :
            tmp = N
        count += tmp
    return count

N = int(input())
K = int(input())

left = 1
right = N ** 2

while left <= right:
    mid = (left + right) // 2
    tmp = find_less(N,mid)
    if tmp >= K :
        ans = mid
        right = mid - 1
    else :
        left = mid + 1
print(ans)