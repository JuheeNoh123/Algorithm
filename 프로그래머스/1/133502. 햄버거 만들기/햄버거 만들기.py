def solution(ingredient):
    answer = 0
    ham = [1,2,3,1]
    stack=[]
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack)>=4 and stack[-4]==ham[0] and stack[-3]==ham[1] and stack[-2]==ham[2] and stack[-1]==ham[3]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer+=1
        

    
        #print(s)
            
            
    return answer