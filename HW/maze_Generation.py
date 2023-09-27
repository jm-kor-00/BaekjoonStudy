import random
class vertex :
  def __init__(self,u,v,w):
    self.u = u
    self.v = v
    self.weight = w
  
  def get_u(self):
    return self.u
  
  def get_v(self):
    return self.v
  
  def get_w(self):
    return self.weight

def generate_maze(width, height):
  visited = []
  MST_vertex = []
  vertex_matrix = [[[]for _ in range(width)]for _ in range(height)]
  
  #간선 무작위 가중치 부여, 저장(가로방향)
  for i in range(height):
    for j in range(width - 1):
      rand_w = random.randrange(1,500)
      v1 = vertex((i,j),(i,j+1),rand_w)
      v2 = vertex((i,j+1),(i,j),rand_w)
      vertex_matrix[i][j].append(v1)
      vertex_matrix[i][j+1].append(v2)
  #간선 무작위 가중치 부여, 저장(세로방향)
  for i in range(height - 1):
    for j in range(width):
      rand_w = random.randrange(1,1000)
      v1 = vertex((i,j),(i+1,j),rand_w)
      v2 = vertex((i+1,j),(i,j),rand_w)
      vertex_matrix[i][j].append(v1)
      vertex_matrix[i+1][j].append(v2)

  #랜덤으로 시작 노드 정하기
  start_x = random.randrange(0,height)
  start_y = random.randrange(0,width)
  #시작노드 방문처리
  visited.append((start_x,start_y))
  

  #prim's MST algorithm
  while len(visited) < height * width: #모든 노드를 방문할 때까지
    #방문한 노드에서 방문하지 않은 노드로 가는 모든 간선을 저장할 리스트
    neighbors = [] 
    #visited에 있는 모든 방문노드에 대해
    for nd in visited:
      x,y = nd[0],nd[1]
      for vtx in vertex_matrix[x][y]:
        #간선의 도착지가 아직 방문하지 않은 노드이면
        if vtx.get_v() not in visited :
          #후보에 추가
          neighbors.append(vtx)
    
    min = float('inf')
    #후보 중에 가중치 제일 작은 간선을 selected로 지정함
    for vtx in neighbors:
      #t_w : 간선의 가중치
      t_w = vtx.get_w()
      if t_w < min :
        #min과 selected 갱신
        selected = vtx
        min = t_w

    #selected 결정 후 MST에 추가
    MST_vertex.append(selected)
    #selected 간선의 목적지인 노드를 방문처리
    visited.append(selected.get_v())

  #미로를 나타낼 2차원 배열
  #True : 길, False : 벽
  maze = [[False for _ in range(width * 2 + 1)]for _ in range(2 * height + 1)]

  #MST에 포함된 모든 간선에 대해
  for vtx in MST_vertex :
    start = vtx.get_u()
    end = vtx.get_v()

    #출발지, 도착지 노드를 True로 갱신
    maze[2 * start[0] + 1][2 * start[1] + 1] = True
    maze[2 * end[0] + 1][2 * end[1] + 1] = True

    #세로 방향 간선의 경우
    if start[0] == end[0]:
      if start[1] < end[1]:
        maze[2 * start[0] + 1][2 * end[1]] = True
      else:
        maze[2 * start[0] + 1][2 * start[1]] = True
    #가로 방향 간선의 경우
    else :
      if start[0] < end[0]:
        maze[2 * end[0]][2 * start[1] + 1] = True
      else:
        maze[2 * start[0]][2 * start[1] + 1] = True

  #미로 입출구 지정
  maze[1][0] = True 
  maze[2 * height - 1][2 * width] = True
  #완성된 미로 반환
  return maze

#미로 출력 함수
def print_maze(maze):
  print()
  for col in maze:
    for el in col:
      if el : print(" ",end=" ")
      else : print("■",end=" ")
    print()
  print()
  
MAZE1 = generate_maze(12,8)
MAZE2 = generate_maze(8,12)
print_maze(MAZE1)
print_maze(MAZE2)