#몇월, 몇일을 구분하여 날짜를 입력받음
month,day = map(int,input("오늘의 날짜는 : ").split())
#각 달이 몇일씩인지를 저장한 리스트
monthly_date = [31,28,31,30,31,30,31,31,30,31,30,31]
#오늘이 몇번째 날인지를 나타낼 변수
today = 0
#반복문으로 지난 달까지의 일 수를 모두 더함
for i in range(month - 1):
    today += monthly_date[i]
#오늘 날짜를 더함
today += day
#결과출력
print("오늘은 2023년의",today,"번째 날입니다.")