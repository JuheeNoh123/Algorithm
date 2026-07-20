def solution(food):
    answer = ''

    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
        
    s=answer[::-1]
    answer+='0'+s

    return answer