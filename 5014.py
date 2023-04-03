from collections import deque
F,S,G,U,D = map(int,input().split())

def BFS(F,S,G,U,D):
    visited = [0] * (F+1)
    queue = deque()
    queue.append(S)
    btn_count = 0
    while queue :
        btn_count += 1
        for i in range(len(queue)):
            tmp = queue.popleft()
            for move in (U,-D):
                next = tmp + move
                if next < 1 or next > F :
                    continue
                if not visited[next]:
                    visited[next] = btn_count
                    queue.append(next)
    return visited[G]

if S == G : print(0)
else :
    result = BFS(F,S,G,U,D)
    print("use the stairs" if result == 0 else result)