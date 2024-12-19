import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, (abs(a),a))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    
