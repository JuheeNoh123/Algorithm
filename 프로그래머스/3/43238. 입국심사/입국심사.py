 
def solution(n, times):
    
    low = min(times)
    high = low*n
    answer = high
    while low<=high:
        mid = (low+high)//2
        if sum(mid//t for t in times) >= n:
            answer = mid
            high = mid-1
        else:
            low = mid+1
    
    return answer