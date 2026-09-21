from collections import deque
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    di, dj = [1,-1,0,0], [0,0,-1,1]
    d = deque([])
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and maps[i][j]!='X':
                #print(visited)
                visited[i][j]=1
                d.append([i,j])
                #print(i,j)
                #섬 연결 탐색
                s = 0
                while d:
                    #print(d)
                    ii,jj = d.popleft()
                    s+=int(maps[ii][jj])
                    for k in range(4):
                        nii = ii+di[k]
                        njj= jj+dj[k]
                        if 0<=nii<n and 0<=njj<m and visited[nii][njj]==0 and maps[nii][njj]!='X':
                            visited[nii][njj]=1
                            d.append([nii,njj])
                            #print(nii,njj)
                answer.append(s)
        if len(answer)==0:
            return [-1]
        answer.sort()
    return answer