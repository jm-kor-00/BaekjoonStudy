NO_OF_CHARS = 128

def shift_table(pat):
    m = len(pat)
    tbl = [m] * NO_OF_CHARS
    
    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    return tbl

def create_good_suffix_table(pattern):
    m = len(pattern)
    table = {}
    suffixes = get_suffixes(pattern)
    for i in range(m - 1):
        suffix = suffixes[i]
        for j in range(1, len(suffix) + 1):
            if suffix[-j] not in table:
                table[suffix[-j]] = j
    for char in pattern:
        if char not in table:
            table[char] = m
    return table

def get_suffixes(pattern):
    m = len(pattern)
    suffixes = []
    for i in range(m - 1):
        suffixes.append(pattern[i + 1:])
    return suffixes

def boyer_moore_search(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    good_suffix_table = create_good_suffix_table(P)
    i = m - 1
    compare = 0
    while i < n:
        k = 0
        while k <= m - 1 and P[m - 1 - k] == T[i - k]:
            k += 1
        compare += k
        if k == m:
            print("문자 비교 횟수:", compare)
            return i - m + 1
        else:
            compare += 1
            if T[i] in good_suffix_table:
                i += max(t[ord(T[i])], good_suffix_table[T[i]])
            else:
                i += t[ord(T[i])]
    print("문자 비교 횟수:", compare)
    return -1

T = "aiflkngkngjlallkadlkasklaeflkafaa"
P = "flkn"

result = boyer_moore_search(T, P)
if result != -1:
    print("패턴이 등장한 위치:", result)
else:
    print("패턴이 텍스트에 존재하지 않습니다.")