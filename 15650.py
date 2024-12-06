N,M = map(int,input().split()); N+=1
tmp = []
def recu(pos,left):
    global tmp
    if left == 0:
        for el in tmp:
            print(el,end=" ")
        print()
    elif pos < N :
        for i in range(pos,N):
            tmp.append(i)
            recu(i+1,left-1)
            tmp.pop()        
recu(1,M)