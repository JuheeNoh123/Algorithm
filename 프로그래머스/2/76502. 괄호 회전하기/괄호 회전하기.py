from collections import deque
def solution(s):
    answer = -1
    L = list(s)
    d = deque(L)
    #print(d)
    res=0
    for i in range(len(d)):
        d.rotate(1)
        stack=[d[0]]
        for j in range(1,len(d)):
            if d[j]=='(' or d[j]=='{' or d[j]=='[':
                stack.append(d[j])
            elif d[j]==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
            elif d[j]=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append('}')
            elif d[j]==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(']')
        if not stack:
            res +=1
    
    return res