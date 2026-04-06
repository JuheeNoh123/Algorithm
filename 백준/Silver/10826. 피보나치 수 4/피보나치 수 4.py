

b = int(input())
a = [0 for _ in range(b+1)]
if b>1:
    a[1] = 1
if b>2:
    a[2] = 1
for i in range(3,b+1):
    a[i] = a[i-1]+a[i-2]
if b>=3:
    print(a[-1])
if b==1 or b==2:
    print(1)
if b==0:
    print(0)