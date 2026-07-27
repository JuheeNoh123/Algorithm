from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    map =[[0] * 102 for _ in range(102)]
    for i in range(len(rectangle)):
        left_under_x = rectangle[i][0]*2
        left_under_y = rectangle[i][1]*2
        right_up_x = rectangle[i][2]*2
        right_up_y = rectangle[i][3]*2
        for j in range(left_under_y, right_up_y+1):
            for k in range(left_under_x, right_up_x+1):
                map[j][k]=1
    for i in range(len(rectangle)):
        left_under_x = rectangle[i][0]*2
        left_under_y = rectangle[i][1]*2
        right_up_x = rectangle[i][2]*2
        right_up_y = rectangle[i][3]*2
        for j in range(left_under_y+1, right_up_y):
            for k in range(left_under_x+1, right_up_x):
                map[j][k]=0
    

    
    
    d = deque([(characterY*2, characterX*2)])
    di, dj = [-1, 1, 0, 0], [0,0,-1,1]
    visited = [[0]*102 for _ in range(102)]
    visited[characterY*2][characterX*2]=1
    while d:
        i,j = d.popleft()
        if i==itemY*2 and j==itemX*2:
            answer = visited[i][j]//2
            break
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<102 and 0<=nj<102 and map[ni][nj]==1 and visited[ni][nj]==0:
                visited[ni][nj]=visited[i][j]+1
                d.append((ni, nj))
    
    # for i in visited:
    #     for j in i:
    #         print(j, end='')
    #     print()
    # print('-----------------------')
    
    return answer