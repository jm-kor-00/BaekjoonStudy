import sys
input = sys.stdin.readline
#피보나치 함수
def fibonacci(n):
    global zero_call, one_call
    if n == 0 :
        zero_call += 1
        return 0
    elif n == 1 :
        one_call += 1
        return 1
    else :
        return fibonacci(n - 2) + fibonacci(n - 1)
#main
zero_call = 0
one_call = 0
T = int(input())
for i in range(T):
    fibonacci(int(input()))
    print(zero_call, one_call)
    zero_call = 0; one_call = 0