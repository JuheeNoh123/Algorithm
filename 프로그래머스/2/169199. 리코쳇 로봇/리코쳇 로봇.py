from collections import deque
def sliding(pos, dir, board):
    directions = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
    dx, dy = directions[dir]
    cur = pos[:]
    while True:
        nx, ny = cur[0]+dx, cur[1]+dy
        if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]) or board[nx][ny]=="D":
            return cur
        cur=[nx, ny]
        
        
def solution(board):
    answer = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                st = [i,j]
            elif board[i][j]=='G':
                ed = [i,j]
    
    d=deque()
    d.append([st,0])
    visited=[[False]*len(board[0]) for _ in range(len(board))]
    visited[st[0]][st[1]]=True    
    while d:
        cur, dist = d.popleft()
        if cur==ed: return dist
        
        for i in range(4):
            next_pos = sliding(cur, i, board)
            if visited[next_pos[0]][next_pos[1]]==False:
                visited[next_pos[0]][next_pos[1]]=True
                d.append([next_pos, dist+1])
    return -1
                