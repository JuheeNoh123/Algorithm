import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
dic={}
for i in range(n):
    s,p = input().strip().split()
    dic[s]=int(p)
sum = 0
for i in range(k):
    s = input().strip()
    if dic.get(s)!=None:
        sum += dic[s]
        del dic[s]
d = sorted(dic.items(), key=lambda x:x[1])

#print(d)
min = sum
max=sum

for i in range(m-k):
    min+=d[i][1]
    max += d[n-k-i-1][1]
print(min,max)