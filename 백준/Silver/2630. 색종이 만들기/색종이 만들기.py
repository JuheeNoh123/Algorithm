import sys

input = sys.stdin.readline


n = int(input())

L = []
for i in range(n):
    r = list(map(int,input().split()))
    
    L.append(r)

white = 0
blue = 0

def sol(x,y,n):
    #print('x,y,n',x,y,n)
    global white
    global blue
    fst = L[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            #print('i,j',i,j)
            if fst != L[i][j]:
                #print('fst!= L[i][j]')
                sol(x,y,n//2)
                sol(x,y+n//2,n//2)
                sol(x+n//2,y,n//2)
                sol(x+n//2,y+n//2,n//2)
                return
    if fst ==0:
        white += 1
    else:
        blue += 1
    
                
sol(0,0,n)
print(white)
print(blue)
            