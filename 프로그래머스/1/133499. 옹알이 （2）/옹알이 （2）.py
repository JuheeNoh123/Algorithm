def solution(babbling):
    answer = 0
    for i in babbling:
        idx=0
        pre=0
        while idx<len(i):
            if i[idx:idx+3]=='aya' and pre!='aya':
                idx+=3
                pre='aya'
            elif i[idx:idx+3]=='woo' and pre!='woo':
                idx+=3 
                pre='woo'
            elif i[idx:idx+2]=='ye' and pre!='ye':
                idx+=2
                pre='ye'
            elif i[idx:idx+2]=='ma' and pre!='ma':
                idx+=2
                pre='ma'
            else:
                break
        if idx==len(i):
            answer+=1
                
    return answer