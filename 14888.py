import sys
from copy import deepcopy as dc
input = sys.stdin.readline


N = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split())) # + - x /

cases = []
def recur(tmp, operator):
    if sum(operator) == 0 : 
        cases.append(tmp)
        return
    for i in range(4):
        if operator[i] != 0:
            left = dc(operator)
            left[i] -= 1
            recur(tmp+str(i),left)

recur("",operator)

MAX = -float('INF')
MIN = float('INF')

for case in cases:
    tmp = nums[0]
    for i in range(len(case)):
        if case[i] == '0':
            tmp += nums[i+1]
        elif case[i] == '1':
            tmp -= nums[i+1]
        elif case[i] == '2':
            tmp *= nums[i+1]
        else :
            if tmp < 0:
                tmp = (-1) * ((-1 * tmp) // nums[i+1])
            else :
                tmp //= nums[i+1]
    
    if tmp > MAX :
        MAX = tmp
    if tmp < MIN :
        MIN = tmp

print(MAX)
print(MIN)