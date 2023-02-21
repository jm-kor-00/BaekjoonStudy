import sys
import heapq as Heap
input = sys.stdin.readline

N = int(input())

#최대힙으로 사용할 리스트
maxH = []
for _ in range(N):
    Heap.heappush(maxH,-(int(input())))
result = 0

for i in range(1,N + 1):
    tmp = -(Heap.heappop(maxH))
    if result < tmp * i :
        result = tmp * i
print(result)