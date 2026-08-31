def solution(skill, skill_trees):
    answer = 0
    
    #t_pointer = 0
    
    for skill_tree in skill_trees:
        s_pointer = 0
        for st in range(len(skill_tree)):
            if s_pointer>=len(skill) or (st==len(skill_tree)-1 and not skill_tree[st] in skill[s_pointer+1:]):
                answer +=1
                print(skill_tree)
                break
            if skill_tree[st] in skill: #B가 있는데
                if skill[s_pointer]!=skill_tree[st]: #선행 스킬이 아직 있음
                    break
                else:
                    s_pointer+=1
                    
                        
        
                    
                
    return answer