def solution(w,h):
    answer = 0
    
    for x in range(1,w):
        #print(p*x)
        answer += int((h*x)/w)
    answer*=2
    
    return answer