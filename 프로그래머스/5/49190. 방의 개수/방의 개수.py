def solution(arrows):
    answer = 0
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    # 0:위 1:오른위 2:오른 3:오른아래 4:아래 5:왼아래 6:왼 7:왼위
    
    x, y = 0, 0
    points = {(0, 0)} # 방문 여부 확인
    edges = set()
    answer = 0
    
    for arrow in arrows:
        nx, ny = x+dx[arrow], y+dy[arrow]
        edge = frozenset({(x,y), (nx, ny)})
        if edge not in edges:
            edges.add(edge)
            if (nx, ny) in points: # 이미 방문한 점으로 연결되면 -> 방 하나 생김
                answer += 1
            points.add((nx, ny))
            
            if arrow %2 ==1: #대각선 이동일때만 교차 체크
                cross_edge = frozenset({(x,ny), (nx, y)})
                if cross_edge in edges:
                    answer +=1
        x,y = nx, ny
    return answer