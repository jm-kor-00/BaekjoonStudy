import sys
input = sys.stdin.readline

class MaxHeap :
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    def size(self): return len(self.heap) - 1
    def isEmpty(self) : 
        if self.size() == 0 : return True
        else : return False
    def Parent(self,i) : return self.heap[i//2]
    def Left(self,i) : return self.heap[i*2]
    def Right(self,i) : return self.heap[i*2 + 1]
    def insert(self,n):
        #맨끝으로 삽입
        self.heap.append(n)
        #현재 n의 위치
        i = self.size()
        while(i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while(child <= self.size()):
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child] : break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
        else :
            return 0
MaxH = MaxHeap()
N = int(input())
for _ in range(N):
    M = int(input())
    if M == 0:
        print(MaxH.delete())
    else:
        MaxH.insert(M)