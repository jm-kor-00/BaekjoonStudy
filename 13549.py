from collections import deque
N,K = map(int,input().split())

def BFS(N,K):
    visited = [False for _ in range(100001)]
    que = deque()
    que.append((K,0))
    visited[K] = 0
    while que :
        tmp,dist = que.popleft()
        # print(tmp,dist)
        if tmp == N : return dist
        t = tmp
        while t % 2 == 0 and t > 0:
            t = t // 2
            if visited[t] != False:
                if visited[t] <= dist : continue
            visited[t] = dist
            que.appendleft((t,dist))

        nxts = [tmp+1,tmp-1]
        for nxt in nxts:
            if not 0 <= nxt <= 100000 : continue
            if visited[nxt] != False:
                if visited[nxt] <= dist + 1 : continue
            visited[nxt] = dist+1
            que.append((nxt,dist+1))
print(BFS(N,K))