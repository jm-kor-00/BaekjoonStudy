import sys
input = sys.stdin.readline

#이걸 모르면
#이진수로 만드는 함수 만들고, 각 자리 비교하는 방식을 써야 됨

def getFlipCount(a:int,b:int,c:int)->int:
    cnt = 0
    #정수의 최대 크기를 고려
    for i in range(0,32):
        pos = 1 << i # ** 시프트로 비트 위치를 맞춤 **
        tmp = c & pos # 우주에서 보낸 신호의 i번째 자리의 값 => 0 or 1
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