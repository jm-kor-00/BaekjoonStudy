import sys
input = sys.stdin.readline

N,M,INVEN = map(int,input().split())
MAP = []
for i in range(N):
    MAP += (list(map(int,input().split())))
g_high = max(MAP)
g_low = min(MAP)
b_sum = sum(MAP) + INVEN
def function(H):
    used = 0
    digged = 0
    for block in MAP:
        if block - H > 0 :
            digged += block - H
        else :
            used += H - block
    return digged * 2 + used

H = min(g_high,b_sum // (M * N)); Highest = H
MIN = function(H)

while(g_low < H):
    H -= 1
    tmp = function(H)
    if tmp < MIN :
        MIN = tmp
        Highest = H
    elif tmp > MIN :
        break
print(MIN,Highest)