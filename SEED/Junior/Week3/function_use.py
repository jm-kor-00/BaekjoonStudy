from recursFunction import recu_factorial as factorial
#1 똑같은 행동을 반복해야 할 때
# 팩토리얼을 계속 구해야 한다.

#직접 입력
n1 = int(input())
factorial_N = 1
#반복문으로 N! 구하기
for i in range(1,n1+1):
    factorial_N *= i
#결과출력
print("%d! ="%n1,factorial_N)

n2 = int(input())
factorial_N = 1
for i in range(1,n2+1):
    factorial_N *= i
print("%d! ="%n2,factorial_N)

n3 = int(input())
factorial_N = 1
for i in range(1,n3+1):
    factorial_N *= i
print("%d! ="%n3,factorial_N)

#함수사용
n1 = int(input())
print("%d! ="%n1,factorial(n1))

n2 = int(input())
print("%d! ="%n2,factorial(n2))

n3 = int(input())
print("%d! ="%n3,factorial(n3))