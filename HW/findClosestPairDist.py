import math
import random

#랜덤으로 n개 좌표를 생성해서 정렬 후 반환하는 함수
def createPairs(n):
    arr = []
    for _ in range(n):
        x = random.randint(1,3 * n)
        y = random.randint(1,3 * n)
        arr.append((x,y))

    return sorted(arr,key=lambda point:point[0]) 

#두 점사이의 거리 반환하는 함수
def distance(p1,p2):
    x1,y1 = p1[0], p1[1]
    x2,y2 = p2[0], p2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#완전탐색으로 최근접쌍 거리 반환
def closest_pair_bruteForce(P):
    MinDist = float('inf')
    for i in range(len(P)):
        for j in range(len(P)):
            if i != j:
                tmp = distance(P[i],P[j])
                if tmp < MinDist:
                    MinDist = tmp
    return MinDist

#이미 오름차순 정렬되어있는 두 리스트를 병합하는 함수
def merge(p1, p2, sort_key):
    key1 = 0
    key2 = 0
    merged = []
    while key1 < len(p1) and key2 < len(p2):
        if p1[key1][sort_key] < p2[key2][sort_key]:
            merged.append(p1[key1])
            key1 += 1
        else :
            merged.append(p2[key2])
            key2 += 1

    if key1 < len(p1):
        merged += p1[key1:]
    else :
        merged += p2[key2:]

    return merged

#띠구간에 대한 최근접쌍 거리를 반환
def strip_closest(P,d):
    n = len(P)
    d_min = d
    for i in range(n):
        j = i + 1
        #P[i].y와 P[j].y의 차이가 d_min 이내일 때까지만 처리
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i],P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

#bruteForce로 구현
def closest_pair(P):
    n = len(P)
    mindist = float('inf')
    #요소는 3개이하로, y축기준 정렬이 들어가도 미미한 연산횟수
    y_sorted = sorted(P,key=lambda point:point[1])

    for i in range(n-1):
        for j in range(i+1,n):
            dist = distance(P[i],P[j])
            if dist < mindist :
                mindist = dist

    return y_sorted, mindist

#구현된 함수
def closest_pair_dist(P,n):
    if n <= 3:
        return closest_pair(P)
    
    mid = n//2
    mid_x = P[mid][0]

    pL, dL = closest_pair_dist(P[:mid], mid)
    pR, dR = closest_pair_dist(P[mid:], n - mid)
    d = min(dL,dR)

    #이미 y축 오름차순인 두 리스트를 병합
    newP = merge(pL,pR,1)
    Ps = []
    #x축 기준, 범위안에 들어오는 좌표들 삽입
    for i in range(n):
        if abs(newP[i][0] - mid_x) < d:
            Ps.append(newP[i])
    #띠 구간 확인
    dS = strip_closest(Ps,d)
    # dS는 초기값이 d이고, d이하임.
    return newP,dS #병합했던 리스트와 이 구간의 최소거리 반환

#main
p = createPairs(int(input('좌표의 개수 : ')))

print("완전탐색으로 찾은 최소쌍 간의 거리 =",closest_pair_bruteForce(p))
print("분할정복으로 구현한 알고리즘으로 찾은 최소쌍 간의 거리 =",closest_pair_dist(p,len(p))[1])