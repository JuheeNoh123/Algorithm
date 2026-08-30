def can(X,stones,k):
    c = 0
    for s in stones:
        if s<X:
            c+=1
            if c>=k:
                return False
        else:
            c=0    
    return True

def solution(stones, k):
    answer = 0
    low = 1
    high = max(stones)
    
    while low<=high:
        mid = (low+high)//2
        if can(mid,stones,k):
            answer=mid
            low = mid +1
        else:
            high = mid-1
        
            
    return answer