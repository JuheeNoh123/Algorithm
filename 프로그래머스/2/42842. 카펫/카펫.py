def solution(brown, yellow):
    answer = []
    for i in range(1,int(yellow**0.5)+1):
        w = i
        h = yellow//w
        if w*h == yellow:
            b = h*2 + w*2 + 4
            if b==brown:
                answer.append(w+2)
                answer.append(h+2)
                answer.sort(reverse=True)
                break
    
    return answer