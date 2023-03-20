import sys
input = sys.stdin.readline

Words = [] #단어들을 저장할 리스트
DICT = {} #알파벳은 dictionary 자료형 사용

#입력
for _ in range(int(input())):
    Words.append(list(input().strip()))

#입력받은 단어들에 대해
for wd in Words :
    #단어의 문자들에 대해
    for i in range(len(wd)):
        #가중치 ex) ABCD에서 A는 1000의 가중치를 가짐
        tmp_val = 10 ** (len(wd) - 1 - i)
        #해당 알파벳이 딕셔너리에 들어있는지 확인
        if wd[i] in DICT:
            DICT[wd[i]] += tmp_val #이미 있으면 value 수정
        else :
            DICT[wd[i]] = tmp_val #아직 없으면 key:value 추가
#(1) 키값들을 리스트로 변환
Values = list(DICT.values())
#(2) 내림차순 정렬
Values.sort(reverse=True)

#가중치 mul, 9부터 0까지 1씩 감소
mul = 9
#총합이 결과
SUM = 0
for el in Values:
    SUM += el * mul
    mul -= 1
#결과출력
print(SUM)