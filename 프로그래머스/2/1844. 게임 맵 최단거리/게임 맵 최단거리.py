from collections import deque
def solution(maps):
    answer = -1
    d = deque()
    d.append([0,0])
    visited=[[False]*len(maps[0]) for _ in range(len(maps))]
    visited[0][0]=True
    di,dj=[-1,1,0,0],[0,0,-1,1]
    cnt=0
    while d:
        i,j = d.popleft()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if ni>=0 and ni<len(maps) and nj>=0 and nj<len(maps[0]):
                if visited[ni][nj]==False and maps[ni][nj]!=0:
                    visited[ni][nj]=True
                    d.append([ni,nj])
                    maps[ni][nj]=maps[i][j]+1
    
    if maps[-1][-1]!=1:
        answer=maps[-1][-1]
    
        
    return answer
