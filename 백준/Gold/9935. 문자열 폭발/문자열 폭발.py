import sys
import heapq
input = sys.stdin.readline

n = input().strip()
a = list(input().strip())
L = []
for i in range(len(n)):
    L.append(n[i])
    if L[len(L)-len(a):]==a:
        for _ in range(len(a)):
            L.pop()
if len(L):
    print(''.join(L))
else:
    print("FRULA")