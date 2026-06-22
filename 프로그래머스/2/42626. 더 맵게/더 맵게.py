import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        cnt+=1
        s = a+b*2
        heapq.heappush(scoville, s)
    return cnt
