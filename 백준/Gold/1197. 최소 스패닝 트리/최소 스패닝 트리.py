import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v,e = map(int, input().split())
edges = []
for i in range(e):
    edges.append(list(map(int,input().split())))
edges.sort(key= lambda x:x[2])

parent =[i for i in range(v+1)]
def find_p(x):
    if parent[x]==x:
        return x
    
    parent[x] = find_p(parent[x])
    return parent[x]

def union_p(a,b):
    a=find_p(a)
    b=find_p(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def same_p(a,b):
    return find_p(a)==find_p(b)

ans=0
for a,b,cost in edges:
    if not same_p(a,b):
        union_p(a,b)
        ans+=cost
print(ans)
        