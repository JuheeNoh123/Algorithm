import heapq

def solution(jobs):
    jobs.sort()
    heap=[]
    count =0
    idx=0
    current_time=0
    total = 0
    while count < len(jobs):
        #현재 시간까지 요청된 작업을 힙에 추가
        while idx < len(jobs) and jobs[idx][0]<=current_time:
            req_time, job_time = jobs[idx]
            heapq.heappush(heap, (job_time, req_time, idx))
            idx+=1
        
        if heap:
            job_time, req_time, _ = heapq.heappop(heap)
            current_time += job_time #작업 완료 시점
            total += current_time - req_time #반환시간 = 완료 - 요청
            count += 1
        else:
            #대기 큐가 비어있으면 다음 요청으로 점프
            current_time = jobs[idx][0]
            

    return total // len(jobs)