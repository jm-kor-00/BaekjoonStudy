N = 10
#0부터 N-1까지 반복
for i in range(0,N):
    print(i)
#증가폭 수정 가능!
for i in range(N,0,-1):
    print(i)
for i in range(-1,N,3):
    print(i)
#특정값안에서 반복
for i in (1,3,7,8):
    print(i)

#for-each문
#리스트의 요소들로 반복:
arr = ['a','b','c','d']
for el in arr:
    print(el)
#증감자를 사용할 필요가 없을 때
for _ in range(0,5):
    print("###")