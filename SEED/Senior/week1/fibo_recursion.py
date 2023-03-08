def fib_recursion(n):
    if n == 0 : return 0
    elif n == 1 : return 1
    else : 
        return fib_recursion(n - 1) + fib_recursion(n - 2)

N = int(input())
print(fib_recursion(N))