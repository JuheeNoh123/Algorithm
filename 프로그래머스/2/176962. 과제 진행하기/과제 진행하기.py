
    
def solution(plans):
    answer = []
    stack = []
    d = {}
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2])*60 + int(plans[i][1][3:])
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x:x[1])
    
    for i in range(len(plans)-1):
        stack.append([plans[i][0],plans[i][2]])
        gap = plans[i+1][1]-plans[i][1]
    
        while stack and gap: #할 과제가 남아있고, 다음 과제까지 시간이 남아있다면 계속 과제 진행
            now = stack[-1][1] #현재 과제하는데에 걸리는 시간
            if now<=gap: #다음 과제까지 시간이 있다면
                n,t = stack.pop() #현재 과제를 끝냄. 
                gap -= t #현재 과제하고 남은 시간으로 업데이트
                answer.append(n) #끝낸 과제 답에 추가
            else: #다음 과제 시작 시간까지 현재 과제를 다 끝낼 수 없다면
                stack[-1][1] -= gap #현재 과제를 남은 시간만큼이라도 함. 
                gap = 0
    stack.append(plans[-1]) #마지막 과제 시작하기     
    #print(stack)
    for i in range(len(stack)-1,-1,-1): #마지막 과제까지 다 시작은 했으니까 stack에 있는 과제들을 뒤에서부터 마무리해줌 
        answer.append(stack[i][0])
        
    #print(plans)
    return answer