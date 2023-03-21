import sys
import heapq as HQ
input = sys.stdin.readline

Deck = []
for _ in range(int(input())):
    HQ.heappush(Deck,int(input()))

result = 0

while len(Deck) > 1 :
    tmp = HQ.heappop(Deck) + HQ.heappop(Deck) 
    result += tmp
    HQ.heappush(Deck,tmp)

print(result)