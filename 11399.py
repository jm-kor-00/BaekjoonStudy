import sys
input = sys.stdin.readline

N = int(input())
list = list(map(int,input().split()))
list.sort()
sum = list[0]
for i in range(1,N):
    list[i] += list[i - 1]
    sum += list[i]
print(sum)