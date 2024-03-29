#0-1 knapsack problem
def knapsack_dp(W,wt,val,n):
    #테이블생성
    knapsack = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            #용량초과시
            if wt[i-1] > w :   
                knapsack[i][w] = knapsack[i-1][w]
            else :
                #추가한 경우와 안한 경우를 저장
                valWith = val[i-1] + knapsack[i-1][w-wt[i-1]]
                valWithout = knapsack[i-1][w]
                #더 큰값 저장
                knapsack[i][w] = max(valWith, valWithout)

    return knapsack[n][W]