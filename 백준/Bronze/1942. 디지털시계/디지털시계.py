
for i in range(3):
    start,end = input().split()
    s_h,s_m, s_s =map(int,start.split(':'))
    e_h,e_m,e_s = map(int,end.split(':'))
    L=[]
    if int(str(s_h)+str(s_m)+str(s_s))%3==0:
        L.append(int(str(s_h)+str(s_m)+str(s_s)))
    while True:
        if s_h==e_h and s_m==e_m and s_s==e_s:
            break
        s_s+=1
        if s_s==60:
            s_s=0
            s_m+=1
        if s_m==60:
            s_m=0
            s_h +=1
        if s_h==24:
            s_h=0
        #print(s_h, s_m,s_s)
        time = int(str(s_h)+str(s_m)+str(s_s))
        if time %3==0:
            L.append(time)

    print(len(L))
            