import sys
from collections import deque

input = sys.stdin.readline


def checking(queue, target):
    count = 1
    while queue:
        tmp = queue.popleft()
        _pop = True
        for el in queue:
            if el[0] > tmp[0]:
                queue.append(tmp)
                _pop = False
                break
        if _pop:
            if tmp[1] == target:
                return count
            else:
                count += 1
    return count


for _ in range(int(input())):
    N, target = map(int, input().split())
    arr = list(map(int, input().split()))
    Queue = deque()
    for i in range(N):
        Queue.append([arr[i], i])

    print(checking(Queue, target))
