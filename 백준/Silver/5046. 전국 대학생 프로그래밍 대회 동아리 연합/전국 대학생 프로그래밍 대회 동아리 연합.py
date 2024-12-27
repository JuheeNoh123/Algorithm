import sys
input = sys.stdin.readline

N, B, H, W = map(int, input().split())
L=[0 for _ in range(H)]
min=10000000
for i in range(H):
    money = int(input())
    av = list(map(int, input().split()))
    pos=0
    for i in av:
        if i>=N:
            pos=1
    if pos==1:
        if money*N<=B and money*N<=min:
            min=money*N
    
if min!= 10000000:
    print(min)
else:
    print("stay home")