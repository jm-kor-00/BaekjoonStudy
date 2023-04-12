import math
def distance(p1,p2):
    x1,y1 = p1[0], p1[1]
    x2,y2 = p2[0], p2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def strip_closest(P,d):
    n = len(P)
    d_min = d
    P.sort(key=lambda point:point[1])

    for i in range(n):
        j = i + 1
        #P[i].y와 P[ㅓ].y의 차이가 d_min 이내일 때까지만 처리
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
    for i in range(n-1):
        for j in range(i+1,n):
            dist = distance(P[i],P[j])
            if dist < mindist :
                mindist = dist
    return mindist

def closest_pair_dist(P,n):
    if n <= 3:
        return closest_pair(P)
    