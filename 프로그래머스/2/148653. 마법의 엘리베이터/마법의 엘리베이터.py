def solution(storey):
    answer = 0
    while storey>0:
        d = storey%10
        storey //= 10
        
        if d<5:
            answer += d
        elif d>5:
            answer += (10-d)
            storey += 1
        else:
            answer += 5
            if storey %10>=5:
                storey += 1
        
            
    return answer