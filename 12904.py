import sys, copy
input = sys.stdin.readline

def soulution(S,T):
    tmp = copy.deepcopy(T)
    while len(S) != len(tmp):
        if tmp[-1] == 'A':
            tmp = tmp[:-1]
        else :
            tmp = tmp[-2::-1]
    for i in range(len(S)):
        if S[i] != tmp[i] : return 0
    return 1

S = list(input().strip())
T = list(input().strip())
print(soulution(S,T))