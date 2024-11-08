import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}    
for i in range(N):
    site, pw = input().split()
    dic[site] = pw
for i in range(M):
    find = input().strip()
    print(dic[find])
    