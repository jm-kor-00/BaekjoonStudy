import sys
input = sys.stdin.readline

function = [[0,0,0,0,0,0,0,0,0,0] for i in range(1001)]
function[1] = [1,1,1,1,1,1,1,1,1,1]
#main
N = int(input())
i = 1
while(i < N) :
    for j in range(0,10):
        for k in range(j,10):
            function[i + 1][k] += function[i][j]
    i += 1
sum = 0
for el in function[N]:
    sum += el
print(sum % 10007)