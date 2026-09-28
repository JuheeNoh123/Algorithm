def solution(dirs):
    answer = 0
    dir = {"U":[-1,0], "D":[1,0], "L":[0,-1], "R":[0,1]}
    visited = set()
    start_i, start_j = 5,5
    i, j = start_i, start_j

    for d in dirs:
        ni, nj = i+dir[d][0], j+dir[d][1]
        if 0<=ni<11 and 0<=nj<11:
            p = sorted([(i,j),(ni,nj)])
            visited.add(tuple(p))
            i,j = ni,nj
        
    return len(visited)