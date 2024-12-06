from collections import deque
import sys
sys.setrecursionlimit(10**6)
def BFS(N,K):
    visited = [False for _ in range(100001)]
    que = deque()
    que.append((N,0))
    while que:
        tmp,s = que.popleft()
        if tmp == K : break
        # if visited[tmp] : continue
        visited[tmp] = True
        nexts = [tmp+1,tmp-1,tmp*2]
        for nxt in nexts:
            if not 0 <= nxt <= 100000:
                continue
            if not visited[nxt]:
                que.append((nxt,s+1))
    ans = 1
    for a,b in que:
        if a == K and b == s:
            ans += 1
    return s,ans
N,K = map(int,input().split())
s,t = BFS(N,K)
print(s)
print(t)