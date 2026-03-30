c, k = map(int, input().split())

d = 10**k
c = c/d
#print(c)
f = c-int(c)
#print(f)
if f>0.4:
    ans = int(c)+1
    ans= ans*(10**k)
else:
    ans = int(c)*(10**k)
print(ans)