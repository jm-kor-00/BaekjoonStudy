import sys
input = sys.stdin.readline

N, M = map(int,input().split())

nums = list(map(int,input().split()))

AddList = []
AddList.append(0)
for i in range(N):
    AddList.append(AddList[i] + nums[i])

for i in range(M):
    H, T = map(int,input().split())
    print(AddList[T] - AddList[H - 1])