def code_cnt(n, size):
    DP = [0] * (size + 1)
    if n[0] > 0:
        DP[1] += 1
    else:
        return 0  
    
    DP[0] = 1
    
    if size == 1:
        return DP[1]
    else:
        for i in range(2, size+1):
            if n[i-1] > 0:
                DP[i] = DP[i-1]
            
            tmp = n[i-2] * 10 + n[i-1]
            # print(tmp)
            if tmp == 0:
                return 0
            elif 10 <= tmp <= 26:
                DP[i] += DP[i-2]

        return DP[size]%1000000

#main
n = list(map(int,input().strip()))
print(code_cnt(n, len(n)))