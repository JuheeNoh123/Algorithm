def solution(dartResult):
    answer = []
    stack = []
    
    flag = False
    for i in range(len(dartResult)):
        if flag:
            flag=False
            continue
        if (ord('0')<= ord(dartResult[i]) and ord(dartResult[i])<=ord('9')): #i가 숫자면
            if i<len(dartResult)-1 and dartResult[i]=='1' and dartResult[i+1]=='0': #i가 10이면
                stack.append(10)
                flag=True
            else:
                stack.append(int(dartResult[i]))
        elif dartResult[i]=='S':
            answer.append(stack[-1])
        elif dartResult[i]=='D':
            answer.append(stack[-1]**2)
        elif dartResult[i]=='T':
            answer.append(stack[-1]**3)
        elif dartResult[i]=='*':
            if len(stack)>=2:
                answer[-1] = answer[-1]*2
                answer[-2] = answer[-2]*2
            else:
                answer[-1] = answer[-1]*2
        elif dartResult[i]=='#':
            answer[-1] = answer[-1]*(-1)
        #print(stack, answer)
    res = sum(answer)
            
    return res