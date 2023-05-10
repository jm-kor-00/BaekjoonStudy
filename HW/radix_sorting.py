from collections import deque
Digit = 96
Queues = [deque() for _ in range(27)]

#큐 리스트에서 순서대로 단어를 리스트에 선형으로 저장하는 함수
def pop_all_el(N):
    global Queues
    poped = []
    out = 0
    for _ in range(N):
        while len(Queues[out]) == 0:
            out += 1
        poped.append(Queues[out].popleft())
    return poped

#기수정렬 함수
def chr_radix_sort(arr, Radix):
    #Queue리스트와 아스키코드값(96) 을 전역화해서 사용
    global Digit, Queues
    #Radix는 기수, 단어의 최대길이
    pos = Radix
    # 1회 반복
    for wd in arr :
        #디폴트 값은 0
        put = 0
        l = len(wd)
        #길이가 충분하면
        if l >= pos:
            put += (ord(wd[pos - 1]) - Digit)
        Queues[put].append(wd)

    #단어길이만큼 반복하게 됨
    while pos > 1:
        pos -= 1
        words = pop_all_el(len(arr))
        for wd in words:
            put = 0
            l = len(wd)
            if l >= pos:
                put += (ord(wd[pos - 1]) - Digit)
            Queues[put].append(wd) 

    #정렬결과를 리스트 형태로 반환함
    return pop_all_el(len(arr))

Dictionary = []
f = open("C:/Users/은재민/git/HW/dictionary.txt",'r',encoding="UTF8")
lines = f.readlines()

Radix = 0
print("=======================================")
print("정렬 전 영단어 리스트, 단어 수 :",len(lines))
print("=======================================")
for el in lines:
    tmp = el.strip()
    print(tmp)
    if len(tmp) > Radix : Radix = len(tmp)
    Dictionary.append(el.strip())
print("=======================================")

afterSorting = chr_radix_sort(Dictionary,Radix)
print("정렬 후")
print("=======================================")
for el in afterSorting :
    print(el)
print("=======================================")