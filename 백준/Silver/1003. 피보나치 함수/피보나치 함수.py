import sys
input = sys.stdin.readline
T = int(input())
L = [[0,0] for _ in range(41)]

L[0] = [1,0]
L[1] = [0,1]
#print(L)
for i in range(T):
    a = int(input())
    for j in range(2,a+1):
        L[j][0] = L[j-2][0] + L[j-1][0]
        L[j][1] = L[j-2][1] + L[j-1][1]
    print(*L[a])
    
    
