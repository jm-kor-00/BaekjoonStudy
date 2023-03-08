import sys
input = sys.stdin.readline

N = int(input())
result = 4
if N == 1 :
    result = 1
for i in range(3,N + 1):
    G_n = 0
    max = int((i**(1/2)) + 1)
    for j in range(1,max):
        if i % j == 0 :
            G_n += (i // j + j)
            if j ** 2 == i :
                G_n -= j
    result += G_n
print(result)