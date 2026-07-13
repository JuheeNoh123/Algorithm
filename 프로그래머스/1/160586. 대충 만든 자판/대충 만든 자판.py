def solution(keymap, targets):
    answer = []
    for target in targets:
        res=0
        flag=1
        for t in target:
            cnt=1000
            for key in keymap:
                try: 
                    cnt = min(cnt, key.index(t))
                    
                except:
                    continue
            if cnt==1000:
                flag=0
                break
            #print(t, cnt)
            
            res += cnt+1
        if flag==0:
            res=-1
            
        answer.append(res)
    return answer