import sys
import heapq
input = sys.stdin.readline

a,b = map(int, input().split())
n = int(input())

L = [[] for _ in range(a+1)]

for i in range(b):
    u, v, w = map(int, input().split())
    L[u].append((v,w))
#print(L)
visited =[0]*(a+1)
# def small():
#     min = 11
#     for i in range(1,a+1):
#         if not visited[i] and min>d[i]:
#             min = d[i]
#             idx = i
#     return idx
d=[int(1e9)]*(a+1)
def dijkstra(start):
    heap=[] #바뀐 경로의 정보를 넣어두는 곳 (2,2),(3,3),(7,4)..
    heapq.heappush(heap,(0,start))
    d[start]=0
    
    while heap:
        #print(heap)
        weight, node = heapq.heappop(heap)
        if weight>d[node]:  #시작 지점과 연결된 간선이 없을경우
            continue
        for i in L[node]:
            cost = weight+i[1]
            if cost<d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))
    
dijkstra(n)        
#print(d)       

for i in range(1,a+1):
    if d[i]==1e9:
        print('INF')
    else:
        print(d[i])