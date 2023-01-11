import sys
input = sys.stdin.readline

function = [[0,0,0,0,0,0,0,0,0,0] for i in range(101)]
function[1] = [0,1,1,1,1,1,1,1,1,1]
#main
N = int(input())
i = 1
while(i < N) :
    function[i + 1][0] = function[i][1]
    function[i + 1][9] = function[i][8]
    for index in range(1,9):
        function[i + 1][index] = function[i][index - 1] + function[i][index + 1]
    i += 1
sum = 0
for el in function[N]:
    sum += el
print(sum % 1000000000)