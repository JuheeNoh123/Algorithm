n, m=map(int, input().split())
L=['' for _ in range(m)]
for i in range(n):
    a = input()
    for j in range(m):
        L[j] += a[j]
#print(L)
cnt =0
for i in range(1,n):
    s = set()
    for j in range(m):
        s.add(L[j][i:])
    #print(s)
    if len(s)==m:
        cnt+=1
    
print(cnt)