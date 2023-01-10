import sys
input = sys.stdin.readline

fibo_list = [[0,0] for i in range(41)]
fibo_list[0] = [1,0]
fibo_list[1] = [0,1]
#main
T = int(input()) #테스트케이스
for i in range(T):
    i = 2
    N = int(input()) #숫자
    if(N <= 1):
        print(fibo_list[N][0],fibo_list[N][1])
    else :
        while(i <= N):
            fibo_list[i][0] = fibo_list[i - 2][0] + fibo_list[i - 1][0]
            fibo_list[i][1] = fibo_list[i - 2][1] + fibo_list[i - 1][1]
            i += 1
        print(fibo_list[N][0],fibo_list[N][1])