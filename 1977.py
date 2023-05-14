from math import sqrt
N = int(input())
M = int(input())

start = int(sqrt(N))
end = int(sqrt(M))
result = []

for i in range(start,end+1):
    if N <= i ** 2 <= M:
        result.append(i**2)

if len(result) == 0 : print(-1)
else :
    print(sum(result))
    print(result[0])