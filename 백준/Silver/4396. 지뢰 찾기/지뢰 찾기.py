import sys

input = sys.stdin.readline


n = int(input())
wlfhl = [list(input().strip()) for _ in range(n)]
open = [list(input().strip()) for _ in range(n)]
dx=[1,-1,0,0,-1,-1,1,1]#남,북, 서, 동, 북서, 북동, 남서, 남동
dy=[0,0,-1,1,-1,1,-1,1]

def wf():
    for i in range(n):
        for j in range(n):
            if wlfhl[i][j]=='*':
                open[i][j]='*'
av=0
for i in range(n):
    for j in range(n):
        if open[i][j]=='x':
            if wlfhl[i][j]=='*':
                av=1
            cnt=0
            #상하좌우, 대각선 살피기
            for z in range(8):
                nx,ny = i+dx[z],j+dy[z]
                if 0<=nx<n and 0<=ny<n:
                    if wlfhl[nx][ny]=='*':
                        cnt+=1
            open[i][j]=cnt
if av==1:
    wf()
for i in open:
    for j in i:
        print(j,end="")
    print()