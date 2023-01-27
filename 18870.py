import sys
input = sys.stdin.readline
N = int(input())
list = list(map(int,input().split()))
tupleList = [[i,list[i]] for i in range(N)]
result = [0] * N

tupleList.sort(key=lambda x: x[1])
# print(tupleList)
result[tupleList[0][0]] = 0

for i in range(1,N):
    result[tupleList[i][0]] = result[tupleList[i - 1][0]]
    if tupleList[i][1] > tupleList[i - 1][1]:
        result[tupleList[i][0]] += 1
for i in range(N):
    print(result[i],end=' ')