import sys
input = sys.stdin.readline

N = int(input())
paper = []
count = [0,0,0]#min,zero,plus = 0
for _ in range(N):
    paper.append(list(map(int,input().split())))

def cutting(N,i,j):
    type = paper[i][j]
    result = True
    for k in range(i,i+N):
        for l in range(j,j+N):
            if paper[k][l] != type : 
                result = False
                break
    if result : 
        count[type + 1] += 1
    else :
        cutting(N//3, i,j)
        cutting(N//3, i,j + (N // 3))
        cutting(N//3, i,j + 2 * (N // 3))
        cutting(N//3, i + N // 3,j)
        cutting(N//3, i + N // 3,j + (N // 3))
        cutting(N//3, i + N // 3,j + 2 * (N // 3))
        cutting(N//3, i + 2 * (N // 3), j)
        cutting(N//3, i + 2 * (N // 3), j + (N // 3))
        cutting(N//3, i + 2 * (N // 3), j + 2 * (N // 3))
cutting(N,0,0)
for el in count:
    print(el)