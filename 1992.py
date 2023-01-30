import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
pic = []
for _ in range(N):
    pic.append(list(map(int,input().strip())))
def quadtree(N,x,y):
    type = pic[x][y]
    success = True
    for i in range(x,x + N):
        for j in range(y,y + N):
            if pic[i][j] != type : 
                success = False
                break
    if success :
        return str(type)
    else :
        return "(" + quadtree(N // 2,x,y) + quadtree(N // 2,x,y + N//2) + quadtree(N // 2, x + N//2, y) + quadtree(N // 2,x + N//2, y + N//2) + ")"
print(quadtree(N,0,0))