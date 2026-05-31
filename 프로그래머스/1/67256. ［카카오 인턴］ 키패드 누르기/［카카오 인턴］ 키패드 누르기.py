def solution(numbers, hand):
    answer = ''
    L_pos = (3,0)
    R_pos = (3,2)
    pos = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    for i in numbers:
        if i==1 or i==4 or i==7:
            L_pos=pos[i]
            answer += 'L'
        elif i==3 or i==6 or i==9:
            R_pos=pos[i]
            answer += 'R'
        else:
            L_dis = abs(L_pos[0]-pos[i][0]) + abs(L_pos[1]-pos[i][1])
            R_dis = abs(R_pos[0]-pos[i][0]) + abs(R_pos[1]-pos[i][1])
            if L_dis>R_dis:
                R_pos=pos[i]
                answer+='R'
            elif L_dis<R_dis:
                L_pos = pos[i]
                answer += 'L'
            else:
                if hand=='right':
                    answer+='R'
                    R_pos=pos[i]
                else:
                    answer +='L'
                    L_pos=pos[i]
    return answer