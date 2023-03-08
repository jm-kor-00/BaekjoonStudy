N = int(input())
#입력
weights = list(map(int,input().split()))
#오름차순 정렬
weights.sort()
#잴 수 있는 무게의 범위
Range = [0,0]
for el in weights:
    #범위의 불연속이 발생할 경우
    if Range[0] + el > Range[1] + 1:
        break
    #범위가 계속 이어질 경우
    else :
        Range[1] += el
#끊어진 부분에서 1 더한값이 답
print(Range[1] + 1)