import sys
from collections import deque
input = sys.stdin.readline

for T in range(int(input())):
    p = list(input().strip())
    p.append('E')
    N = int(input())
    arr = input().strip()
    nums = deque()    
    if N != 0:
        arr = arr[1:len(arr) - 1]; arr = list(map(int,arr.split(',')))
        for el in arr:
            nums.append(el)
    Error = False
    REVERSED = 1
    for i in range(len(p)):             
        if p[i] == 'R':
            REVERSED *= -1
        elif p[i] == 'D':
            if len(nums) == 0:
                Error = True
                break
            if REVERSED > 0 :
                nums.popleft()
            else :
                nums.pop()
    if Error : print("error")
    elif len(nums) > 0 :
        if REVERSED > 0 : 
            print("[",end='')
            for j in range(len(nums) - 1):
                print(nums[j],end=',')
            print(nums[len(nums) - 1],end='')
            print("]")
        else :
            print("[",end='')
            for j in range(len(nums) - 1,0,-1):
                print(nums[j],end=',')
            print(nums[0],end='')
            print("]")
    else :
        print("[]")