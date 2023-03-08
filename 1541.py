import sys
input = sys.stdin.readline

result = 0
init = list(input().split('-'))
result = [0] * len(init)
for i in range(len(init)):
    tmp = list(map(int,(init[i].split('+'))))
    for num in tmp:
        result[i] += num
total = result[0]
for i in range(1,len(result)):
    total -= result[i]
print(total)