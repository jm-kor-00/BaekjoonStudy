<<<<<<< HEAD
arr = list(range(1,31))
for i in range(28):
    input_ = int(input())
    arr[input_ - 1] = 0

for el in arr:
    if el != 0:
        print(el)
=======
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
>>>>>>> 0ef0d32c0c135775a3a01fc2919df7fa7d3a39c2
