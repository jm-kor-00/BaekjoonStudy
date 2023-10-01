import sys
input = sys.stdin.readline

def getResult(N, pairs):
    model = [[] for _ in range(N)]
    MAX_H = 0
    res = ""

    for i in range(N):
        s,e,h = pairs[2*i], pairs[2*i] + pairs[2*i + 1], pairs[2*i + 1]
        tmp_H = 0
        
        for j in range(i):
            if (model[j][1] <= s or model[j][0] >= e):
                continue
            else :
                tmp_H = max(tmp_H,model[j][2])

        model[i] = [s, e, tmp_H + h]
        MAX_H = max(MAX_H,model[i][2])
        res += str(MAX_H) + " "

    return res

for _ in range(int(input())):
    N = int(input())
    pairs = list(map(int,input().split()))
    print(getResult(N,pairs))