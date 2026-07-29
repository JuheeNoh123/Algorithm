import heapq
def solution(n, works):
    answer = 0
    if sum(works)==0:
        return 0
    heap=[-i for i in works]
    heapq.heapify(heap)
    
    #print(works)
    for i in range(n):
        top = -heap[0]
        if top==0:
            break
        heapq.heapreplace(heap, -(top-1))
        
        #print(works)
    for i in heap:
        answer += (-i)**2
    return answer