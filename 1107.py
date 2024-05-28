import sys
from itertools import product
input = sys.stdin.readline

def find(N, available, length):
    Min = abs(N - 100)
    best = 100
    for pdt in product(available, repeat=length):
        tmp = ""
        for el in list(pdt):
            tmp += str(el)
        tmp = int(tmp)
        if abs(N - tmp) + length < Min:
            Min = abs(N - tmp) + length
            best = tmp
    return Min

def solution():
    N = int(input())
    B = int(input())
    if B > 0 :
        broken = set(list(map(int, input().split())))
    if N == 100:
        return 0
    if B == 0:
        return min(len(str(N)), abs(N-100))
    
    available = set([i for i  in range(10)]) - broken
    length = len(str(N))

    Mins = []
    for leng in range(length -1,length+2,1):
        if leng <= 0 or leng > 6:
            continue
        Mins.append = find(N, available, leng)
    return min(Mins)

print(solution())