import sys
input = sys.stdin.readline

n = int(input())
L = []
for i in range(n):
    a = int(input())
    L.append(a)
L.sort()
#print(L)
max = -1
for i in range(n-1,1,-1):
    #print(i)
    if L[i]<L[i-1]+L[i-2]:
        a = sum(L[i-2:i+1])
        if max < a:
            max = a 
            break 
        
    else:
        max = -1
print(max)