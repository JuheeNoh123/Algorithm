def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        
        while stack and stack[-1][1]>prices[i]:
            p = stack.pop()
            answer[p[0]]=i-p[0]
        
        stack.append([i,prices[i]])
    
    for i in range(len(stack)):
        answer[stack[i][0]] = len(prices)-stack[i][0]-1
    return answer