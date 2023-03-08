import sys
input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    if N == 0 : print(N); continue
    closet = []
    item,kind = input().split()
    closet.append([kind,item])
    for _ in range(N-1):
        exist = False
        item, kind = input().split()
        for el in closet:
            if el[0] == kind:
                el.append(item)
                exist = True
                break
        if not exist : closet.append([kind,item])
    result = 1
    for el in closet:
        result *= len(el)
    print(result - 1)