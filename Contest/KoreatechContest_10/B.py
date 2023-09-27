import sys
input = sys.stdin.readline

def getFlipCount(a,b,c):
    cnt = 0
    #정수의 최대 크기를 고려
    for i in range(0,32):
        pos = 1 << i
        tmp = c & pos
        if tmp == 0:
            if a & pos :
                cnt += 1
            if b & pos :
                cnt += 1
        elif not (a & pos or b & pos):
                cnt += 1

    return cnt

for _ in range(int(input())):
    a, b, c = map(int,input().split())
    print(getFlipCount(a,b,c))