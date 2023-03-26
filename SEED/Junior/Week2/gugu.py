arr = list(range(1,31))
for i in range(28):
    input_ = int(input())
    arr[input_ - 1] = 0

for el in arr:
    if el != 0:
        print(el)