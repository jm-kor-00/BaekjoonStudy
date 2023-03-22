import sys
input = sys.stdin.readline

#사람 명수
N = int(input())

arr = list(map(int,input().split()))
arr.sort()
#오름차순으로 입력을 정렬함

sum = 0
for i in range(N-1):
    arr[i + 1] += arr[i] #뒷사람은 (앞사람+앞사람이 기다린 시간)만큼 더 기다림
    sum += arr[i]
sum += arr[N-1]

print(sum)