import random
arr = []
while(True):
    tmp = input()
    if tmp == 'q': break
    arr.append(tmp)
    
count = 0
while count < 6:
    n = random.randrange(0,len(arr))
    print("딸기 :",arr.pop(n))
    count += 1

while count < 12:
    n = random.randrange(0,len(arr))
    print("초코 :",arr.pop(n))
    count += 1