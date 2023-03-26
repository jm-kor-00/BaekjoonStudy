def biSearch_right(arr,num):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > num:
            right = mid - 1
        else :
            left = mid + 1
    return right

def biSearch_left(arr,num):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        else :
            right = mid - 1
    return left

# 근데 이거
# 파이썬 bisect모듈의 bisect_right(left) 랑 똑같아요