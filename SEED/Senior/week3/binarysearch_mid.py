def biSearch_isNum(num, arr):
    #list안에 num을 찾는 이분탐색 함수
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else :
            return True
    return False