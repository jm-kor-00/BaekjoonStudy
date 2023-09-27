N = int(input())
arr = list(map(int,input().split()))

arr_up = sorted(arr)
print(arr_up)
M = max(arr_up)
 
for i in range(1, N):
	S = arr_up[i]
	res = (S-M)/M*100
	print(res)