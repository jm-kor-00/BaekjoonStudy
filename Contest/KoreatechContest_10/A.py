import sys
input = sys.stdin.readline

def count_X(num:int)->int:
    res = ((((num % 100) % 90) % 50 ) % 40 ) // 10
    return res

#main
for _ in range(int(input())):
    B = int(input())
    boxes = list(map(int,input().split()))
    
    total = 0
    for el in boxes:
        total += count_X(el)
    
    print(total)