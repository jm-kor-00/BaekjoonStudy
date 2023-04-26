def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]

    return A

A = [1,4,4,7,21,8,1]
print(selection_sort(A))