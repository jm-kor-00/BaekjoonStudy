import sys
input = sys.stdin.readline

Words = [] #단어들을 저장할 리스트
DICT = {} #알파벳은 dictionary 자료형 사용

#입력
for _ in range(int(input())):
    Words.append(list(input().strip()))

#입력받은 단어들에 대해
for wd in Words :
    #단어에 알파벳들에 대해
    for i in range(len(wd)):
        #가중치 ex) ABCD에서 A: 1000의 가중치
        tmp_val = 10 ** (len(wd) - 1 - i)
        #해당 알파벳이 딕셔너리에 들어있는지 확인
        if wd[i] in DICT:
            DICT[wd[i]] += tmp_val #이미 있으면 value 수정
        else :
            DICT[wd[i]] = tmp_val #아직 없으면 key:value 추가
#키값들을 리스트로 변환
VAL = list(DICT.values())
#내림차순 정렬
VAL.sort(reverse=True)

#9부터 1씩 감소하며 곱해준다
mul = 9
#총합이 결과
SUM = 0
for el in VAL:
    SUM += el * mul
    mul -= 1
#결과출력
print(SUM)