def solution(s):
    answer = 1e9
    
    
    l = len(s)
    if l==1:
        answer=1
    else:
        for i in range(1,l): #몇개씩 자를것인가
            dp=[]
            for j in range(0,l,i): #i만큼 건너뛰며 dp 넣기
                if len(dp)!=0 and s[j:j+i]==dp[-1][0]:
                    dp[-1][1] +=1
                else:
                    dp.append([s[j:j+i], 1])
            #print(dp)
            ans = 0
            for j in dp:
                if j[1]==1:
                    ans += len(j[0])
                else:
                    ans += len(j[0])+len(str(j[1]))

            #print(ans)
            if answer>ans:
                answer = ans
    return answer