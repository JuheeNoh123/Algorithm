import sys
input = sys.stdin.readline

from math import sqrt

a = int(input())
L = []
for i in range(a):
    L.append(float(input()))
    
L.sort()

for i in range(7):
    print(f"{L[i]:.3f}")