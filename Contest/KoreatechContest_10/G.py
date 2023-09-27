import sys
input = sys.stdin.readline

BoardSize = 8

def checkRow(board):
    for i in range(BoardSize):
        if ('X' in board[i]) or ('R' in board[i]) :
            continue
        else:
            return True
    return False  
        
for _ in range(int(input())):
    board = []
    for _ in range(BoardSize):
        board.append(list(input()))
    print('B' if checkRow(board) else 'R')