#break는 반복문을 탈출!
for i in range(10):
    if i > 5 :
        break
    print(i)

#for / while 상관없이 사용가능
j = 0
while True:
    if j > 3:
        break
    print(j)
    j += 1

#continue는 이하 행동을 생략!
for i in range(0,10):
    print(i)
    if i > 5 : continue
    print(i,"는 5이하의 숫자")