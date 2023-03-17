import sys
input = sys.stdin.readline

N = int(input())
table = []
for i in range(N):
    s,e = map(int, input().split())
    table.append([s,e])

count = 0 #회의 개수
cur_end = 0 #현재까지 종료시간

#시작시간으로 오름차순 -> 종료시간으로 오름차순
table.sort(key=lambda a: a[0])
table.sort(key=lambda a: a[1])

# print(table)
for S,E in table:
    if S >= cur_end:
        cur_end = E
        count += 1

print(count)