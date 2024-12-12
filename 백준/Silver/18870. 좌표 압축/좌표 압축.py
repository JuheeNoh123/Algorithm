import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
L2 = sorted(list(set(L)))
dic = {}
for i in range(len(L2)):
    dic[L2[i]]=i
ans = []
for i in L:
    ans.append(dic[i])
print(*ans)