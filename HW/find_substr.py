def bruteForce(arr):
    count = 0
    for i in range(len(arr)):
        #A를 발견하면
        if arr[i] == 'A':
            #A가 있는 곳 뒤에서
            for j in range(i+1,len(arr)):
                #B를 발견하면
                if arr[j] == 'B':
                    #count 1 증가
                    count += 1
    return count

def myPS(arr):
    A_cnt = 0 #A를 발견하면 증가시킬 변수
    total = 0 #A로 시작해서 B로 끝나는 substring의 개수
    for el in arr:
        #A를 발견할 때 마다
        if el == 'A':
            A_cnt += 1
        #B를 찾을 때 마다
        elif el == 'B':
            #substring의 개수를 A_cnt만큼 증가시킴
            total += A_cnt
    return total

#main
if __name__ == "__main__":
    arr = list(input("검사할 문자열을 입력 : ").strip())
    print("억지기법으로 검사한 결과 :",bruteForce(arr))
    print("개선된 방법 :",myPS(arr))