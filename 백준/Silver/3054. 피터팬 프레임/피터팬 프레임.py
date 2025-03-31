import sys
from collections import deque
input = sys.stdin.readline

N = input().strip()

L = [['.' for _ in range(4*len(N)+1)]for _ in range(5)]
for n in range(len(N)):
    if (n+1)%3==0:
        l='*'
    else:
        l='#'
    if n==len(N)-1:
        last=l
    for i in range(5):
        a = 4*n
        if i==0 or i==4:
            L[i][2+a]=l
        if i==1 or i==3:
            L[i][1+a]=l
            L[i][3+a]=l
        if i==2:
            L[i][a]=l
            L[i][2+a]=N[n]
            if L[i-1][a-1]=='*':
                L[i][a]='*'
L[2][-1]=last
for i in L:
    for j in i:
        print(j,end='')
    print()  
