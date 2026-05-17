def solution(phone_book):
    answer = True
    d={}
    for i in phone_book:
        d[i] = 1
    for i in phone_book:
        s=''
        for n in i:
            s += n
            if s in d and s!=i:
                answer=False
    return answer