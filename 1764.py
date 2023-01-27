import sys
input = sys.stdin.readline

N, M = map(int,input().split())
heard = []
seen = []
nor = []
for _ in range(N):
    heard.append(input().strip())
for _ in range(M):
    seen.append(input().strip())
heard.sort()
seen.sort()
h_pos = 0
s_pos = 0
while h_pos < N and s_pos < M:
    if heard[h_pos] == seen[s_pos]:
        nor.append(seen[s_pos])
        s_pos += 1; h_pos += 1
    elif heard[h_pos] > seen[s_pos]:
        s_pos += 1
    else :
        h_pos += 1
print(len(nor))
for el in nor:
    print(el)