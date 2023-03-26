#증감변수를 따로 지정해줘야함!!
i = 0
while i < 10:
    print(i)
    i = i + 1 #i += 1

#무한루프에 빠지지 않도록 주의할 것!!!

#조건에 True넣으면 무한루프가 됨
#이럴땐 꼭 탈출 조건이 필요!
while True :
    N = int(input('숫자입력 :'))
    if N > 10 : break #