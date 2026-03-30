a = int(input())
L = list(map(int, input().split()))
p = L[0]
L.pop(0)
L.sort()
#print(L)
for i in range(a-1):
    if p>L[i]:
        p+=L[i]
        L[i] = 0

if sum(L)>0:
    print("No")
else:
    print("Yes")