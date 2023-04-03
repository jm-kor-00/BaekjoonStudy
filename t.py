def factorial(N):
    if N == 1 : return 1
    else : N * factorial(N-1)

def fibonacci(N):
    if N == 0 : return 0
    if N == 1 : return 1
    else : return fibonacci(N-1) + fibonacci(N-2)

def mycode(N):
    if N == 0 : return 0
    if N == 1 : return 1
    else : return mycode(N-2) * mycode(N-1) + mycode(N-1)

