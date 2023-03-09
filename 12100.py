import sys
input = sys.stdin.readline

N = int(input()) #보드 사이즈
BOARD = [] #입력받을 최초보드
result = [] #각 변환완료된 보드에서 가장 큰 값들을 저장할 리스트

#보드입력
for _ in range(N):
    BOARD.append(list(map(int,input().split())))

#상하좌우 중 한 방향으로 보드를 변환하는 함수
def move(tmp,dir):
    global N #사이즈 N을 전역변수로 사용
    #변환결과를 입력할 새로운 보드
    AFTER = [[0 for _ in range(N)]for _ in range(N)]
    #한번 합쳐진 값들은 다시 합쳐지지 않게 하기위해, 합쳐진 적이 있는 지를 저장하는 2차원 리스트
    united = [[False for _ in range(N)]for _ in range(N)]
    #up
    if dir == 0:
        #i는 열, j는 행
        for i in range(N):
            #같은 값이 연속되어서 합쳐지거나
            #연속되지 않아서 안합쳐진 채로 AFTER에 들어가야 함
            #AFTER에 들어갈 때는 한쪽 벽에 쫙 붙어있어야 하므로
            #place라는 변수를 벽쪽에 가까운 임계값(0 or N-1)으로 생성해서
            #place자리에 넣은 후, place를 1증가시킴 => 벽쪽부터 빈자리없이 채워지게됨
            place = 0
            for j in range(N):
                #빈칸이거나 합쳐진 적이 있는 경우 continue
                if tmp[j][i] == 0 or united[j][i] : continue
                #일단 넣을 자리에 현재 값 넣음
                AFTER[place][i] = tmp[j][i]
                #그 자리부터 벽사이에 있는 값들에 대해 탐색
                for k in range(j + 1,N):
                    #빈칸이 아닌 것을 발견하면
                    if tmp[k][i] != 0:
                        #만약 그 값이 tmp[j][i]와 같다면
                        if tmp[k][i] == tmp[j][i]:
                            #넣었던 값을 2배(=같은 값을 합침)
                            AFTER[place][i] *= 2
                            #합친 것들은 모두 united를 True로 갱신
                            united[j][i] = True
                            united[k][i] = True
                        break
                place += 1
    #down
    elif dir == 1:
        for i in range(N):
            place = N-1
            for j in range(N-1,-1,-1):
                if tmp[j][i] == 0 or united[j][i] : continue
                AFTER[place][i] = tmp[j][i]
                for k in range(j-1,-1,-1):
                    if tmp[k][i] != 0:
                        if tmp[k][i] == tmp[j][i]:
                            AFTER[place][i] *= 2
                            united[j][i] = True
                            united[k][i] = True
                        break
                place -= 1
    #left 
    elif dir == 2:
        for i in range(N):
            place = 0
            for j in range(N):
                if tmp[i][j] == 0 or united[i][j] : continue
                AFTER[i][place] = tmp[i][j]
                for k in range(j + 1,N):
                    if tmp[i][k] != 0:
                        if tmp[i][k] == tmp[i][j]:
                            AFTER[i][place] *= 2
                            united[i][j] = True
                            united[i][k] = True
                        break
                place += 1
    #right  
    else :
        for i in range(N):
            place = N-1
            for j in range(N-1,-1,-1):
                if tmp[i][j] == 0 or united[i][j] : continue
                AFTER[i][place] = tmp[i][j]
                for k in range(j-1,-1,-1):
                    if tmp[i][k] != 0:
                        if tmp[i][k] == tmp[i][j]:
                            AFTER[i][place] *= 2
                            united[i][j] = True
                            united[i][k] = True
                        break
                place -= 1
    #변환결과(2차원배열)를 반환
    return AFTER

#2048 재귀함수, 작명센스 구리네
def tzfe(tmp_board,count):
    #5번 변환완료된 보드라면
    if count == 0:
        #보드의 최대값을 찾아서
        MAX = 0
        for el in tmp_board:
            temp = max(el)
            if temp > MAX : MAX = temp
        #result에 삽입 후, 종료
        result.append(MAX);return
    # 4방향(상하좌우)에 대해 변환한 보드를 가지고
    # count(남은 변환횟수)를 1 감소시키고
    # 재귀호출
    for i in range(4):
        tzfe(move(tmp_board,i),count-1)
#결과
#함수실행
tzfe(BOARD,5)
#result의 최대값이 최적해
print(max(result))