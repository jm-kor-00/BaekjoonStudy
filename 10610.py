import sys
import heapq as Heap
input = sys.stdin.readline

road = input().strip()
isThree = 0
maxH = []
for el in road:
    tmp = int(el)
    isThree += tmp
    Heap.heappush(maxH,-tmp)

if isThree % 3 == 0 and '0' in road:
    while maxH:
        print(-Heap.heappop(maxH),end='')
else :
    print(-1)