import sys
input = sys.stdin.readline

N = int(input())
dic = {}
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    if dic.get(a)==None and b==1:
        dic[a]=b
    elif dic.get(a)==1 and b==0:
        dic[a]=b
    elif dic.get(a)==0 and b==1:
        dic[a]=b
    else:
        cnt += 1
for k in dic:
    if dic[k]==1:
        cnt += 1
print(cnt)
    