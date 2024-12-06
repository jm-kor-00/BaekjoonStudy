# triangle = [[1],[2,3],[4,5,6]]
# def solution(triangle):
#     answer = 0
#     DP = [[0 for _ in range(len(triangle[n]))] for n in range(len(triangle))]
#     print(DP)
#     return answer
    
# solution(triangle)
# import math
# print(math.ceil(3.1))

lst = [[i,100-i] for i in range(100)]
print(lst)
lst.sort(key=lambda x:x[1])
print(lst)

list(map(int,input().split()))
input().strip() #