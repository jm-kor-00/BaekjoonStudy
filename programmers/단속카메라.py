def solution(routes):
    routes.sort(key=lambda x:x[1])
    pos = -30001
    cnt = 0
    for route in routes:
        if route[0] > pos:
            cnt += 1
            pos = route[1]

    return cnt