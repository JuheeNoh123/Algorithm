import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(1,M+1):
    a,b,w = map(int,input().split())
    graph[a].append([b, w])

start, end = map(int, input().split())
ws = [1e9 for _ in range(N+1)]

heap = []
ws[start] = 0
heapq.heappush(heap,[0,start])

while heap:
    cur_w, cur_v = heapq.heappop(heap)  #이전 비용와 직전 노드 빼기
    if ws[cur_v] < cur_w:
        continue
    for next_v,next_w in graph[cur_v]:
        sum_w = cur_w + next_w
        if sum_w >= ws[next_v]:
            continue
        
        ws[next_v] = sum_w
        heapq.heappush(heap,[sum_w,next_v])
      
print(ws[end])