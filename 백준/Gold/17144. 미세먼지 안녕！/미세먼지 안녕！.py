import sys
input = sys.stdin.readline


R,C,T = map(int,input().split())
A = [(list(map(int, input().split()))) for _ in range(R)]

def spread(i,j,m):
    di, dj = [0,0,1,-1], [1,-1,0,0]
    cnt=0
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<R and 0<=nj<C and A[ni][nj]!=-1:
            #A[ni][nj]+=A[i][j]//5
            A[ni][nj]+=m//5
            if m//5>0:
                cnt +=1
    if (m//5) * cnt<=A[i][j]:
        A[i][j]-=(m//5) * cnt

    
dv = [(-1, 0), (0,1), (1,0), (0,-1)]
def up_cleaner(x, y):
    global A
    v, d = 0, 1
    while True:

        nx = x + dv[d][0]
        ny = y + dv[d][1]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d = (d + 3) % 4     # 반시계 방향으로 회전
            continue

        else:
            if A[nx][ny] == -1: # 이동한 곳이 공청기라면
                return
            
            tmp = A[nx][ny] # 현재 위치의 값 저장
            A[nx][ny] = v     # 이전 위치값 변경
            v = tmp             # 현재 위치에 원래 있던 값으로 업데이트
            x, y = nx, ny
              
    
def down_cleaner(x, y):
    global A
    v, d = 0, 1
    while True:

        nx = x + dv[d][0]
        ny = y + dv[d][1]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d = (d + 1) % 4     # 시계 방향으로 회전
            continue

        else:
            if A[nx][ny] == -1:
                return
            tmp = A[nx][ny] # 현재 위치의 값 저장
            A[nx][ny] = v     # 이전 위치값 변경
            v = tmp             # 현재 위치에 원래 있던 값으로 업데이트
            x, y = nx, ny
               



            
for _ in range(T):
    m = []
    s=[]
    for i in range(R):
        for j in range(C):
            if A[i][j]!=0 and A[i][j]!=-1:
                m.append((i,j,A[i][j]))
            if A[i][j]==-1:
                s.append([i,j])
            
    for k in m:             
        spread(k[0],k[1],k[2])
   
    up_cleaner(s[0][0], 0)
    down_cleaner(s[1][0], 0)

ans=0
for i in A:
    ans+=sum(i)
print(ans+2)