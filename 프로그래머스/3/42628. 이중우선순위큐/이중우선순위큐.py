import heapq

def solution(operations):
    
    min_heap = []
    max_heap = []
    for i in operations:
        o, n = i.split()
        if o=='I':
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, -int(n))
        elif o=='D':
            if n=='-1' and min_heap:
                r = heapq.heappop(min_heap)
                max_heap.remove(-r)
                heapq.heapify(max_heap)
            elif n=='1' and max_heap:
                r = heapq.heappop(max_heap)
                min_heap.remove(-r)
                heapq.heapify(min_heap)
    if not min_heap:
        return [0,0]
    return [-max_heap[0], min_heap[0]]