NO_OF_CHARS = 128

def bruteforce_string_search(T,P):
    n = len(T)
    m = len(P)
    compare = 0
    for i in range(n -  m + 1):
        compare += 1
        if T[i] == P[0]:
            j = 0
            while j < m and T[i+j] == P[j]:
                j += 1
            compare += j
            if j == m : 
                print("문자 비교 횟수 :",compare)
                return i
    print("문자 비교 횟수 :",compare)
    return -1

def horspool_search(T,P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    compare = 0
    while(i<=n-1):
        k = 0
        while k<=m-1 and P[m-1-k] == T[i-k]:
            k+=1
        compare += k
        if k == m:
            print("문자 비교 횟수 :",compare)
            return i-m+1
        else:
            i+=t[ord(T[i])]
    print("문자 비교 횟수 :",compare)
    return -1

def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS
    
    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    
    return tbl

T = "I_LOVE_BANANA_YOU_LIKE_APPLE_AND_MANGO"
P = "GRAPE"

print("검색 대상 :",T)
print("찾는 문자열 :",P)
print("===========================================")
print("억지 기법 문자열 탐색 결과")
print("위치 ",bruteforce_string_search(T,P))
print("===========================================")
print("호스풀 알고리즘 탐색 결과")
print("위치 :",horspool_search(T,P))