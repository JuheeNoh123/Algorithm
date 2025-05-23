import sys
input = sys.stdin.readline

N = input().strip()
L = []
for i in N:
    if not (i in '+-*/'):
        L.append(i)
    else:
        b = int(L.pop())
        a = int(L.pop())
        if i=='+':
            r = a+b
        elif i=='-':
            r=a-b
        elif i=='*':
            r=a*b
        else:
            r=a//b
        L.append(r)
print(L[0])