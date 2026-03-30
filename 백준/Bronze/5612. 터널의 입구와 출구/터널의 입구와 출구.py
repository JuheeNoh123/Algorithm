n = int(input())
m = int(input())
Max = m
flag = 0
for i in range(n):
    a, b = map(int, input().split())
    m += a
    m -= b
    if m<0:
        flag = 1
    #print(m)
    Max = max(m,Max)
    #print(Max)

if flag==1:
    print(0)
else:
    print(Max)