#시간,분
hour, min = map(int,input().split())

min = min - 45 # Min -= 45
#음수이면
if min < 0 :
    #60을 더하고
    min = min + 60
    hour = hour - 1 #시간 1 빼기
    #시간이 음수면 23으로 초기화 
    if hour < 0 : hour = 23

print(hour,min)