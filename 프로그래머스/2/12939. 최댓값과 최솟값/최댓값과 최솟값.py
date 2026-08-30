def solution(s):
    answer = ''
    L = list(map(int, s.split()))
    #print(L)
    answer = str(min(L)) +' '+ str(max(L))
    return answer