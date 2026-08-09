def solution(n, stations, w):
    answer = 0
    covered = 0
    for station in stations:
        s = station-w
        e = station+w
        if covered+1<s:
            gap = s-1-covered
            answer += -(-gap//(w*2+1))
        covered = max(e,covered)
    
    if covered<n:
        gap = n-covered
        answer += -(-gap//(w*2+1))
    return answer