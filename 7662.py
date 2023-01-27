import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    visited = [False] * K
    minH = []; maxH = []
    for i in range(K):
        order, num = input().split()
        num = int(num)
        if order == 'I':
            heapq.heappush(minH, (num,i))
            heapq.heappush(maxH, (-num,i))
            visited[i] = True
        else :
            if num == 1:
                while maxH and not visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = False
                    heapq.heappop(maxH)
            else :
                while minH and not visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = False
                    heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    if not minH or not maxH:
        print("EMPTY")
    else:
        MAX = -maxH[0][0]
        MIN = minH[0][0]
        print(MAX,MIN)