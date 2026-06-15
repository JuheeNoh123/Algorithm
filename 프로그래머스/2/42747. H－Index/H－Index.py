def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    r = len(citations)
    for i in range(r):
        if i+1<=citations[i]:
            answer = i+1
        else:
            break
            
    return answer