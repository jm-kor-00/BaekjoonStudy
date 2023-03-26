N = 10
# range란?
# range(N) = 0, 1, 2,..., N-1

# 디폴트 : range(0,N,1)

# range(start,end,increase)는 
# start부터 end-1까지 increase간격으로 있는 모든 정수를 반환하는 함수

#0부터 10까지, 간격 : 1
# arr = list(range(10))
# print("arr =",arr)

#10부터 0까지, 간격 : -1
# brr = list(range(10,0,-1))
# print("brr =",brr)

#0부터 10까지, 간격 : 2
# crr = list(range(0,10,2))
# print("crr =",crr)

#for문의 기본 형태
#리스트의 요소들로 반복:

# print("[arr]")
# for i in arr:
#     print(i)

# arr = ['a','b','c','d']
# print("arr =",arr)
# for el in arr:
#     print(el)

#for문과 range()의 혼용
# print("[0부터 N까지]")
# for i in range(N):
#     print(i)

# print("[N부터 0까지]")
# for i in range(N,0,-1):
#     print(i)

# print("[0부터 N까지, 3간격]")
# for i in range(0,N,3):
#     print(i)

#특정값안에서 반복
# print("[100,230,410,55을 순환]")
# for i in (100,230,410,55):
#     print(i)


#증감변수가 필요없을 때
# for _ in range(0,5):
#     print("###")

#i는 반복문 안에서만 사용한다!

# for i in range(5):
#     print(i)
# print("i =",i)

#근데 이거 왜 돼냐... 파이썬은 신인가? => X
#쓰지말아요 우리. 제발