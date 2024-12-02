from itertools import combinations

n = int(input())
L = []
for i in range(1,11):
    for j in combinations(range(10),i):
        num = ''.join(list(map(str,reversed(list(j)))))
        L.append(int(num))

L.sort()
if n>=len(L):
    print(-1)
else:
    print(L[n])