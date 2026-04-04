a,b,c = map(int, input().split(':'))
cnt=0
flag=True
if a>59 or b>59 or c>59:
    flag = False
if 0<a and a<=12:
    cnt+=1
if 0<b and b<=12:
    cnt += 1
if 0<c and c<=12:
    cnt+=1

if flag:
    if cnt==0:
        print(0)
    elif cnt==1:
        print(2)
    elif cnt==2:
        print(4)
    else:
        print(6)
else:
    print(0)