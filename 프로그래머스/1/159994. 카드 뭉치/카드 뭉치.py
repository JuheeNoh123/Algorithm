def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in range(len(goal)):
        
        #print(goal[i], cards1, cards2)
        if cards1 and goal[i]==cards1[0]:
            cards1.pop(0)
        elif cards2 and goal[i]==cards2[0]:
            cards2.pop(0)
        else:
            answer="No"
            break
    
        
    return answer