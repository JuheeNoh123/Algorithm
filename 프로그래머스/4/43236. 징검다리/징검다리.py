def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    answer = 0
    low = 0
    high = distance
    while low<=high:
        cnt = 0
        mid = (low+high)//2
        prev = 0
        for i in range(1,len(rocks)):
            if rocks[i]-prev < mid:
                cnt +=1
            else:
                prev = rocks[i]
        if cnt<=n:
            if answer<mid:
                answer = mid
            low = mid + 1   #가능하니까 더 크게 간격을 늘려보기
        else:
            high = mid - 1  #불가능하니까 더 작게 간격을 줄여보기
        
    return answer