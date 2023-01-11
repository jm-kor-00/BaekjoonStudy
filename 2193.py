import sys
input = sys.stdin.readline

N = int(input())
Pinary_Nums = [[0,0] for i in range(91)]
Pinary_Nums[1] = [0,1]

i = 1
while(i < N) :
    Pinary_Nums[i + 1][0] = Pinary_Nums[i][1] + Pinary_Nums[i][0]
    Pinary_Nums[i + 1][1] = Pinary_Nums[i][0]
    i += 1
print(Pinary_Nums[N][0]+Pinary_Nums[N][1])