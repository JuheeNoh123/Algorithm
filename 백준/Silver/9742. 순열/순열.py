import sys
from itertools import permutations
input = sys.stdin.readline
while True:
    L = input().strip().split()
    if len(L) != 2:
        break
    n = L[0]
    f = int(L[1])
    idx =0
    flag = False
    for i in permutations(sorted(n),len(n)):
        idx+=1
        if idx==f:
            print(f"{n} {f} = {''.join(i)}")
            flag=True
            break
    if not flag:
        print(f"{n} {f} = No permutation")
            

