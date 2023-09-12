from collections import deque
import sys

input = sys.stdin.readline


def bracketCheck(arr):
    stack = deque()
    stack.append("F")
    for ch in arr:
        if ch == "(":
            stack.append(ch)
        else:
            if stack.pop() == "F":
                return False

    return stack.pop() == "F"


for _ in range(int(input())):
    arr = list(input().strip())
    if bracketCheck(arr):
        print("YES")
    else:
        print("NO")
