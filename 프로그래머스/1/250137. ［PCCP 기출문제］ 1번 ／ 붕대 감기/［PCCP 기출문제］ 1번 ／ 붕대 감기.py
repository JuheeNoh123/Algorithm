def solution(bandage, health, attacks):
    answer = 0
    
    cont=0
    
    hp = health
    idx=0
    last_monster = attacks[-1]
    for i in range(last_monster[0]+1):
        next_monster = attacks[idx]
        if i==next_monster[0]:
            cont=0
    
            hp -= next_monster[1]
            idx+=1
        else:
            cont+=1
            hp+=bandage[1]
            if cont==bandage[0]:
                hp+=bandage[2] #연속 성공시 추가 체력
                cont=0
            if hp>=health:
                hp=health #최대 체력 제한
                #cont=0
                
        print(i,hp, cont, next_monster)
        if hp<=0:
            break
    if hp>0:
        answer=hp
    else:
        answer=-1
    return answer