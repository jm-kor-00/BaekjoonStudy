import sys
from itertools import product, combinations
input = sys.stdin.readline

def isIntersect(set1,set2):
    if set2 <= set1: return True
    return False

def solution():
    basic = ['a','c','i','n','t']
    all = list('abcdefghijklmnopqrstuvwxyz')
    complement = list(set(all) - set(basic))

    # print(complement)
    N, K = map(int,input().split())

    words = []
    for _ in range(N):
        word = input().strip()
        words.append(set(list(word[4:-4])) - set(basic))

    if K < 5 : return 0
    MAX = 0
    for com in combinations(complement,K-5):
        tmpSet = set(list(com))
        cnt = 0
        for word in words:
            if isIntersect(tmpSet,word) : cnt += 1
        # print(tmpSet,"=-----",cnt)

        if cnt > MAX : 
            MAX = cnt
    return MAX
print(solution())