def solution(n, s):
    if n>s:
        return [-1]
    answer = [s//n]*n
    #print(answer)
    for i in range(s%n):
        answer[i] += 1
    #print(answer)
    answer.sort()
    return answer