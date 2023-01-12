import sys
input = sys.stdin.readline
firstline = []
secondline = []

T = int(input())
for i in range(T):
    N = int(input())
    firstline = list(map(int,input().split()))
    secondline = list(map(int,input().split()))
    if N == 1 :
        print(max(firstline[0],secondline[0]))
    else :
        firstline[1] += secondline[0]
        secondline[1] += firstline[0]
        for i in range(2,N):
            firstline[i] += max(secondline[i-1],secondline[i-2])
            secondline[i] += max(firstline[i-1],firstline[i-2])
        print(max(firstline[N-1],secondline[N-1]))    