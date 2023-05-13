from knapsack_memo import knapsack
from knapsack_table import knapsack_dp

val = [60,100,190,120,200,150,300,50,70,100]
wt = [2,5,8,4,7,6,10,6,3,4]
W = 18
n = len(val)

print("======================================================")
print("각 물건 가치 :",val)
print("각 물건 무게 :",wt)
print("배낭용량 :",W)
print("======================================================")
print("메모지에이션을 통한 구현(Top-Down) : ",end='')
print(knapsack(wt,val,W))
print("======================================================")
print("테뷸레이션을 통한 구현(Bottom-Up) : ",end='')
print(knapsack_dp(W,wt,val,n))