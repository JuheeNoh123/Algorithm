def solution(x):
    answer = True
    s = str(x)
    sum = 0
    for i in s:
        sum += int(i)
    if x%sum!=0:
        answer = False 
    return answer