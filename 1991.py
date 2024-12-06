import sys
input = sys.stdin.readline

class node:
    def __init__(self,alph,left,right):
        self.left = left
        self.right = right
        self.ch = alph

    def setLeft(self,lft):
        self.left = lft

    def setRight(self,rgt):
        self.right = rgt

N = int(input())
nodes = {}
for i in range(N):
    nodes[chr(65+i)] = node(chr(65+i),'.','.')
for _ in range(N):
    root,left,right = map(str,input().strip().split())
    if left != '.':
        nodes[root].setLeft(nodes[left])
    if right != '.':
        nodes[root].setRight(nodes[right])

def preorder(root):
    if root == '.' : return
    print(root.ch,end='')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == '.' : return
    inorder(root.left)
    print(root.ch,end='')
    inorder(root.right)

def postorder(root):
    if root == '.' : return
    postorder(root.left)
    postorder(root.right)
    print(root.ch,end='')

preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])