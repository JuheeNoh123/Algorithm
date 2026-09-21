def solution(s):
    answer = []
    
    count = 0
    zero = 0
    while True:
        if s=='1':
            break
        for i in s:
            if i=='0':
                count +=1
                
        s = bin(len(s.replace('0','')))[2:]
        print(s)
        zero+=1
    answer = [zero,count]
    return answer