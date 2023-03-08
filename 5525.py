import sys
input = sys.stdin.readline
N = int(input())
S = int(input())
result = 0
line = list(input().strip())
i = 0
while(i < S):
    if line[i] == 'I':
        tmp = i
        count = 0
        while(tmp + 2 < S):
            if line[tmp + 1] == 'O':
                tmp += 1
                if line[tmp + 1] == 'I':
                    tmp += 1
                    count += 1
                else :
                    break     
            else:
                break
        i = tmp + 1
        if count > N :
            result += (count - N + 1)
        elif count == N : result += 1
    else : i += 1
print(result)