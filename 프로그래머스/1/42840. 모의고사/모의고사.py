def solution(answers):
    answer = []
    f = [1,2,3,4,5]
    s = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        x1 = i%5
        x2 = i%8
        x3 = i%10
        if answers[i]==f[x1]:
            cnt1+=1
        if answers[i]==s[x2]:
            cnt2+=1
        if answers[i]==t[x3]:
            cnt3 +=1
    
    m = max(cnt1, cnt2, cnt3)
    if m==cnt1:
        answer.append(1)
    if m==cnt2:
        answer.append(2)
    if m==cnt3:
        answer.append(3)
    return answer