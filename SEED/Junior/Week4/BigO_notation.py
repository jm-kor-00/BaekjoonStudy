#1
# 리스트에서 10을 찾는 알고리즘
def findNum(num):
    arr = [1,4,2,6,7,8,9,10,5,3]

    for i in range(0,len(arr)):
        if arr[i] == 10:
            return True
    
    return False

#2
A = [1,4,2,6,7,8,9,10,5,3]
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

#3
def gcd(a,b):
    A = []
    B = []
    for i in range(2,a):
        if a % i == 0 :
            A.append(a)

    for i in range(2,b):
        if b % i == 0 :
            B.append(b)
    
    gcd = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                if A[i] > gcd :
                    gcd = A[i]
    
    return gcd