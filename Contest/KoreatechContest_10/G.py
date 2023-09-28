import sys
input = sys.stdin.readline

BoardSize = 8

#풀 수 있는 방법이 많음(문제 조건 굉장히 널널)
#어쨌든 한 행, 혹은 한 열이 연속되는 부분을 찾아내기만 하면 됨

#행 확인
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