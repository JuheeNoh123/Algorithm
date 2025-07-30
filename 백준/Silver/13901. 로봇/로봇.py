import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())  #방의 크기
k = int(input()) #장애물 개수
room = [['*' for _ in range(C)] for _ in range(R)]  #방 크기 (x(C):행, y(R):열)

#장애물 위치 0으로 삽입
for _ in range(k):
    br,bc= map(int, input().split())
    room[br][bc]=0


sr, sc = map(int,input().split()) #시작 위치 입력
a,b,c,d = map(int,input().split()) #상하좌우 순서 입력


dir=deque()
dir.append(a)
dir.append(b)
dir.append(c)
dir.append(d)
#print(direction)

room[sr][sc]=1
queue = deque([[sr,sc]])
while True:
    #print(queue)
    x,y = queue.popleft()
    can = 0
    
    for _ in range(4):
        if dir[0]==1:
            nx=x-1
            ny=y
        elif dir[0]==2:
            nx=x+1
            ny=y
        elif dir[0]==3:
            nx=x
            ny=y-1
        else:
            nx=x
            ny=y+1
        #print("nx,ny",nx,ny)
        #print(R)
        if 0<=nx<R and 0<=ny<C and room[nx][ny]=='*': 
            #print(dir)
            can=1
            room[nx][ny]=room[x][y]+1
            
            queue.append([nx,ny])
            break
        else:
            dir.rotate(-1)
            #print(dir)

            
    #print(room)
        
    if can==0:
        print(x,y)
        break

