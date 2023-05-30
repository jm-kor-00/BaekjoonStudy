from collections import deque

BOARD = [[1,0,1,1,1,1],
         [1,0,1,0,1,0],
         [1,0,1,0,0,1],
         [1,1,1,0,1,1]]
 
start = (0,0) #출발점
end = (3,5) #도착점

#BFS로 구현한 미로탐색 함수
def mazeSearch(board,start,end):
    #행,열 개수 구함
    R = len(board) - 1
    C = len(board[0]) - 1

    #상하좌우 4방향 이동에 사용할 배열
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    #방문처리에 사용할 배열
    visited = [[False for _ in range(C+1)] for _ in range(R+1)]
    #시작점 방문처리
    visited[start[0]][start[1]] = True

    queue = deque()
    queue.append(start)
    
    while(queue):
        x,y = queue.popleft()
        #도착점에 방문했으면
        if (x,y) == (end):
            #탐색 종료
            print("종점 도착 가능")
            return True
        #4방향으로 이동한 좌표에 대해 탐색할 것
        for i in range(4):
            #tx,ty는 순서대로
            #(x+1,y),(x-1,y),(x,y+1),(x,y-1)
            tx = x + dx[i]
            ty = y + dy[i]

            #보드 사이즈를 넘어가는 경우
            if tx < 0 or tx > R or ty < 0 or ty > C :
                continue

            #방문하지 않았고, 접근가능(값 : 1)한 경우
            if not visited[tx][ty] and board[tx][ty] == 1:
                queue.append((tx,ty))
                visited[tx][ty] = True
    
    # while문 탈출 == 종점 도착 못한채 탐색 종료됨
    print("종점 도착 불가능")
    return False

mazeSearch(BOARD,start,end)