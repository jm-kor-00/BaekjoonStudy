A = list(input())
B = list(input())
C = list(input())
D = list(input())

right = 2
left = 6


def move(gear,dir):
    arr = [0] * 8
    #시계방향
    if dir == 1:
        arr[0] = gear[7]
        for i in range(1,7):
            arr[i] = gear[i-1]
    else :
        arr[7] = gear[0]
        for i in range(1,7):
            arr[i] = gear[i+1]

def act(gear, dir):
    global A,B,C,D
    tmp_A = A
    tmp_B = B
    tmp_C = C
    tmp_D = D
    if gear == 1:
        tmp_A = move(A,dir)
        if A[right] == B[left]:
            tmp_B = move(B,-dir)
            if B[right] == C[right] :
                tmp_C = move(C,dir)
                if C[right] == D[right] :
                    tmp_D = move(D,-dir)
    elif gear == 2:
        tmp_B = move(B,dir)
        if A[right] == B[left]:
            tmp_A = move(A,-dir)
        if B[right] == C[left]:
            tmp_C = move(C,dir)
            if C[right] == D[right] :
                tmp_D = move(D,-dir)
                    
for _ in range(int(input())):
    tar, dir = map(int,input().split())
