from random import randint
import random
import copy

class cla:
    #생산자 메소드 작성 필요
    def __init__(self):
         pass
    
    def mergeSort3(self, A, S, low, high):
    #A : 랜덤한 수가 들어있는 리스트
    #S : A와 길이가 같은 0으로 초기화된 리스트
    #low = 0, high =  len(A) - 1
        if (high - low) < 2:
            return 0
        else:
            mid1 = low + ((high - low) // 3)
            mid2 = low + 2 * ((high - low) // 3)
            self.mergeSort3(A, S, low, mid1)
            self.mergeSort3(A, S, mid1 + 1, mid2)
            self.mergeSort3(A, S, mid2 + 1, high)
            
            self.merge3(A, S, low, mid1, mid2, high)

    def merge3(self, A, S, low, mid1, mid2, high):
        i = s = low
        j = mid1 + 1
        k = mid2 + 1
        while i <= mid1 and j <= mid2 and k <= high:
            print(S)
            if A[i] < A[j] and A[i] < A[k]:
                S[s] = A[i]
                i += 1
                s += 1
            elif A[j] < A[k]:
                S[s] = A[j]
                j += 1
                s += 1
            else:
                S[s] = A[k]
                k += 1
                s += 1

        while i <= mid1 and j <= mid2:
            if A[i] <= A[j]:
                    S[s] = A[i]
                    i += 1
                    s += 1
            else:
                S[s] = A[j]
                j += 1
                s += 1
        
        while i <= mid1 and k <= high:
            if A[i] <= A[k]:
                    S[s] = A[i]
                    i += 1
                    s += 1
            else:
                S[s] = A[k]
                k += 1
                s += 1
        
        while k <= high and j <= mid2:
            if A[k] <= A[j]:
                    S[s] = A[i]
                    k += 1
                    s += 1
            else:
                S[s] = A[j]
                j += 1
                s += 1
        
        S[s : s + mid1 - i + 1] = A[i : mid1 + 1]
        S[s : s + mid2 - j + 1] = A[i : mid2 + 1]
        S[s : s + high - k + 1] = A[i : high + 1]

        A[low : high + 1] = S[low : high + 1]   

def testMergeSort():
    a = cla()
    A = random.sample(range(1, 30), 15)
    S = [0] * len(A)
    print("Original  : ", A)
    a.mergeSort3(A, S, 0, len(A)-1)
    print("MergeSort_rec : ", A)

def main():
     testMergeSort()

if __name__ == '__main__':
    main()