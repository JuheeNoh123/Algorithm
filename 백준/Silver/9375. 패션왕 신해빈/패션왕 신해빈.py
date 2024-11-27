import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    dic = {}
    n = int(input())
    for _ in range(n):
        val, key = input().split()
        if not dic.get(key):
            dic[key] = [val]
        else:
            dic[key].append(val)
    cnt = 1
    for i in dic:
        cnt *= len(dic[i])+1
    
    print(cnt-1)