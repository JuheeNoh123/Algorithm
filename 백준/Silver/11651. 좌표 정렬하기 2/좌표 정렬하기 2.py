N = int(input())
L = []

for _ in range(N):
      x,y = map(int, input().split())
      L.append((x,y))

L.sort(key = lambda l:(l[1],l[0]))
for x,y in L:
      print(x,y)