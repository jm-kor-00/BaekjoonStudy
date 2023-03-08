import sys
class Node():
    def __init__(self, n, prv = None, nxt = None):
        self.data = n
        self.prev = prv
        self.next = nxt
class DoubleLinkedQueue():
    def __init__(self):
        self.root = None
    def isEmpty(self):
        if self.root == None : return True
        else : return False
    def insert(self, num):
        #비었을때
        if self.isEmpty() :
            self.root = Node(num)
        else :
            #1개있을때
            if self.root.next == None:
                node = Node(num,self.root,self.root)
                self.root.next = node
                self.root.prev = node
                if self.root.data > num :
                    self.root = node
                return
            #2개이상
            else :
                #루트변경
                if(num <= self.root.data):
                        node = Node(num,self.root.prev,self.root)
                        node.prev.next = node
                        self.root.prev = node
                        self.root = node
                        return
                #나머지
                tmp = self.root.next
                while(tmp != self.root):
                    if num <= tmp.data :
                        node = Node(num,tmp.prev,tmp)
                        tmp.prev.next = node
                        tmp.prev = node
                        return     
                    tmp = tmp.next
                node = Node(num, self.root.prev,self.root)
                self.root.prev.next = node
                self.root.prev = node                
    def pop(self,order) :
        #0개
        if self.isEmpty() :
            return
        #1개
        if self.root.next == None:
            self.root = None
            return
        #2개
        if self.root.next == self.root.prev :
            if order == -1:
                self.root = self.root.next
            self.root.next = None
            self.root.prev = None
            return  
        #3개이상 min
        if order == -1:
            self.root.prev.next = self.root.next
            self.root.next.prev = self.root.prev
            self.root = self.root.next
        #max
        else :
            self.root.prev.prev.next = self.root
            self.root.prev = self.root.prev.prev
    def result(self):
        if self.isEmpty() :
            print("EMPTY")
            return
        if self.root.next == None :
            print(self.root.data,self.root.data)
        else :
            print(self.root.prev.data,self.root.data)
    def clear(self):
        self.root = None
    def printout(self):
        if self.isEmpty() : return
        tmp = self.root
        print(tmp.data)
        tmp = tmp.next
        while(tmp != self.root and tmp != None):
            print(tmp.data)
            tmp = tmp.next
T = int(sys.stdin.readline())
queue = DoubleLinkedQueue()
for t in range(T):
    queue.clear()
    k = int(sys.stdin.readline())
    for i in range(k):
        j,o = map(str,sys.stdin.readline().split())
        if j == 'I':
            queue.insert(int(o))
        else :
            queue.pop(int(o))
        # print("----------")
        # print("현재 큐")
        # print("----------")
        # queue.printout()
        # print("----------")
    queue.result()