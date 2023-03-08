#break는 반복문을 탈출!
for i in range(0,10):
    if i > 5 :
        break
    print(i)
j = 0
while True:
    if j > 3:
        break
    print(j)
    j += 1

#continue는 밑에 블록을 생략!
for i in range(0,10):
    print(i)
    if i > 5 : continue
    print(i,"는 5이하의 숫자")