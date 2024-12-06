from collections import deque
A,B = map(int,input().split())

def BFS(A,B):
    que = deque()
    que.append((B,1))

    while que:
        t,cnt = que.popleft()
        if t == A : return cnt
        if t < A : continue
        if t % 2 == 0 :
            que.append((t//2,cnt+1))
        elif t % 10 == 1:
            que.append((t//10,cnt+1))

    return -1      

print(BFS(A,B))