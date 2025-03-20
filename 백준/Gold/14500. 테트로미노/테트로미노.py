import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
tets = [[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],
        [(0,1),(1,0),(1,1)],
        
        [(1,0),(1,1),(2,1)],[(0,-1),(1,-1),(1,-2)],
        [(1,0),(1,-1),(2,-1)],[(0,1),(1,1),(1,2)],
        
        [(1,0),(2,0),(2,1)],[(0,1),(0,2),(1,0)],
        [(0,1),(1,1),(2,1)],[(0,1),(0,2),(-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)],
        [(1,0),(2,0),(0,1)],[(1,0),(1,1),(1,2)],
        
        [(1,0),(1,1),(1,-1)],[(1,0),(1,1),(2,0)],
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)]]

def cals(i,j,tet):
    temp = L[i][j]
    for di, dj in tet:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M:
            temp += L[ni][nj]
        else:
            return 0
    return temp
    
ans = 0
for i in range(N):
    for j in range(M):
        for tet in tets:
            temp = cals(i,j,tet)
            ans = max(temp, ans)
print(ans)