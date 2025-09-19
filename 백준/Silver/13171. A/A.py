import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
x = int(input())

def b(x):
    #print(x)
    if x==1:
        return n
    h = b(x//2)
    if x%2==1:
        return h**2 * n % 1000000007
    else:
        return h**2 % 1000000007
    

print(b(x))