def solution(schedules, timelogs, startday):
    answer = 0
    ok_schedules=[]
    a = len(schedules)
    for i in range(a):
        s = schedules[i]%100 +10
        h = schedules[i]//100
        if s%100>=60:
            s %= 60
            h += 1
        if h>=24:
            h=0
        ok_schedules.append(h*100+s)
    print(ok_schedules)
    l = len(timelogs)
    for i in range(l):
        flag=True
        for j in range(7):
            currentday = (j+startday)%7
            #print(currentday)
            if currentday==6 or currentday==0:
                continue
            
            if timelogs[i][j]>ok_schedules[i]:
                flag=False
                break
            #print(flag)
        if flag:
            answer+=1
    return answer