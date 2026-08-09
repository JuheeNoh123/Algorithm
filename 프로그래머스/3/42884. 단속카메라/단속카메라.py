def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    cam = -30001
    for s,e in routes:
        if not s<=cam<=e:
            answer+=1
            cam = e
    return answer