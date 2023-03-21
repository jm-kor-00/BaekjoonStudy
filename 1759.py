import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int,input().split())
arr = sorted(list(input().split()))

word = list(combinations(arr,L))
for el in word:
    tmp = ""
    conso = 0
    vowel = 0

    for ch in el:
        if ch in ['a','e','i','o','u']:
            vowel += 1
        else : conso += 1
        tmp += ch
    if vowel > 0 and conso > 1 :
        print(tmp)