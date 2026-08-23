from collections import deque
def solution(m, n, puddles):
    answer = 0
    L = [[0]* m for _ in range(n)]
    for j,i in puddles:
        L[i-1][j-1] = -1
    L[0][0]=1
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            if L[i][j]==-1:
                L[i][j] = 0
                continue
            
            up = L[i-1][j] if i>0 else 0
            left = L[i][j-1] if j>0 else 0
            
            L[i][j] = (up+left)%1000000007
    return L[n-1][m-1]