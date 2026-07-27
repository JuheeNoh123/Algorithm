def solution(game_board, table):
    n = len(game_board)

    def get_blocks(board, target):
        visited = [[False]*n for _ in range(n)]
        blocks = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    # DFS로 덩어리 하나 뽑기
                    stack = [(i, j)]
                    visited[i][j] = True
                    points = []
                    while stack:
                        y, x = stack.pop()
                        points.append((y, x))
                        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                            ny, nx = y+dy, x+dx
                            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == target and not visited[ny][nx]:
                                visited[ny][nx] = True
                                stack.append((ny, nx))
                    blocks.append(points)
        return blocks

    def normalize(points):
        min_y = min(p[0] for p in points)
        min_x = min(p[1] for p in points)
        return sorted((y-min_y, x-min_x) for y, x in points)

    def rotate(points):
        return normalize([(x, -y) for y, x in points])

    holes = get_blocks(game_board, 0)   # 빈 칸 덩어리들
    pieces = get_blocks(table, 1)       # 퍼즐 조각 덩어리들

    used = [False] * len(pieces)
    answer = 0

    for hole in holes:
        hole_shape = normalize(hole)
        print(hole_shape)
        for idx, piece in enumerate(pieces):
            if used[idx]:
                continue
            shape = normalize(piece)
            matched = False
            for _ in range(4):
                shape = rotate(shape)
                if shape == hole_shape:
                    matched = True
                    break
            if matched:
                used[idx] = True
                answer += len(hole)
                break

    return answer