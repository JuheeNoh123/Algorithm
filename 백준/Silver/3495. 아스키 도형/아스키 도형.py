import sys
input = sys.stdin.readline

h, w = map(int, input().split()) 
L=[]
for i in range(h):
    L.append(input().strip())

half = 0
cnt=0
for i in range(h):
    lines=0
    for j in range(w):
        if L[i][j]=='/' or L[i][j]=='\\':
            half +=1
            lines += 1
        else:
            if lines%2==1:
                cnt+=1
print(cnt+half//2)
