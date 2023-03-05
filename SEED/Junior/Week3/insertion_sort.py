arr = [3,1,6,4,9,7,8,5,2]
#길이 : 9
n = 9
for i in range(1,n):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else : break
print(arr)
# j는 1,2,...,8,9
# 시그마 n?