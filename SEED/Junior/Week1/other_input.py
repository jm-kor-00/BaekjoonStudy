
# year, month, day = map(int,input("년,월,일을 띄어쓰기로 구분해서 입력:").split())
# print(year,"년",month,"월",day,"일")
#map(자료형,input().split())
#split은 문자열을 잘라주는 녀석
#split() == split(' ')

# name1, name2, name3 = input("최애 아이돌 3명 입력 : ").split()
# print(name1,name2,name3)

# uni1, uni2, uni3 = map(str,input("대학교 이름을 쉼표로 구분해서 입력 : ").split(','))
# print(uni1,uni2,uni3)

# 너, 시험점수 다 대봐
score = list( map(int,input("시험점수 다 입력해봐:").split()) )
# 100 200 300 40 20 ...
print(score)

# 너 친구이름 다 대봐
friends = list(map(str,input("친구이름 다대봐 :").split()))
print(friends)