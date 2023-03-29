#반복문으로 구현한 팩토리얼
def i_factorial(N):
    fn = 1
    for i in range(1,N+1):
        fn *= i
    return fn

#재귀로 구현한 팩토리얼
def r_factorial(N):
    if N == 1: return 1
    else : return N * r_factorial(N-1)

#반복문으로 구현한 피보나치
def i_fibonacci(N):
    fb = [0] * (N+1)
    fb[1] = 1
    fb[2] = 1
    for i in range(N+1):
        fb[i] = fb[i-1] + fb[i-2]

    return fb[N] 

#재귀로 표현한 피보나치
def r_fibonacci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    else :
        return r_fibonacci(N-1) + r_fibonacci(N-2)