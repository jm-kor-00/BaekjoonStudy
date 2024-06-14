from collections import deque
visited = []

def isPossible(A,B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    if cnt == 1 : return True
    return False

def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    que = deque()
    
    for i in range(len(words)):
        if isPossible(begin,words[i]):
            que.append((i,1))
            visited[i] = True

    while que:
        t,dis = que.popleft()
        if words[t] == target : return dis

        for i in range(len(words)):
            if visited[i] : continue
            if t == i : continue
            if isPossible(words[t],words[i]):
                visited[i] = True
                que.append((i,dis+1))
                
    return 0