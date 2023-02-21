import sys
import heapq as Heap
input = sys.stdin.readline

N = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

low_price = price[0]
result = 0
for i in range(N-1):
    if price[i] < low_price:
        low_price = price[i]
    result += low_price * dist[i]
print(result)