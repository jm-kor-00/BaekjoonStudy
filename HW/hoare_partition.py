arr = [5,3,8,4,9,1,6,2,7]

def partition(arr,left,right):
    low = left + 1
    high = right
    pivot = arr[left]
    while low <= high :
        while low <= right and arr[low] < pivot : low += 1
        while high >= low and arr[high] > pivot : high -= 1

        if low < high :
            arr[low], arr[high] = arr[high], arr[low]
            
    arr[left],arr[high] = arr[high],arr[left]
    print(arr)
    return high

print(partition(arr,0,8))