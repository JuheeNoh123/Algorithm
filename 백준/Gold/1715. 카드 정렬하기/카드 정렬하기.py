import sys
import heapq
input = sys.stdin.readline

n = int(input())
L=[]

for _ in range(n):
    L.append(int(input()))
heapq.heapify(L)

sum = 0
while len(L)>1:
    first = heapq.heappop(L)
    second = heapq.heappop(L)
    sum += first+second
    heapq.heappush(L,first+second)
    #print(L)
print(sum)