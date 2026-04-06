n,m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
L = list(a-b)
L.sort()
print(len(L))
for i in L:
    print(i, end=' ')
