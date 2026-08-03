def solution(new_id):
    answer = ''
    n1=''
    for i in new_id:
        if ord('A')<=ord(i)<=ord('Z'):
            re = chr(ord(i)+32)
            #print(re)
            n1+=re
        else:
            n1+=i
    #print('n1',n1) 
    n2=''
    for re in n1:
        if ord('a')<=ord(re)<=ord('z') or ord('0')<=ord(re)<=ord('9') or re in ['.','-','_']:
            n2+=re
    #print('n2',n2)
    n3=''
    cnt=0
    i=0
    while i<len(n2):
        next_i=i+1
        if n2[i]=='.':
            cnt=1
            while next_i<len(n2) and n2[next_i]=='.':
                cnt +=1
                next_i+=1
        if cnt>1:
            n3+='.'
        else:
            n3+=n2[i]
        cnt=0
        i=next_i
    #print("n3",n3)
    n4=n3
    if len(n3)==1 and n3[0]=='.':
        n4=''
    elif len(n3)>1:
        if n3[0]=='.':
            n4 = n3[1:]
            print(n4)
        if n3[-1]=='.':
            n4=n4[:len(n4)-1]
    #print("n4",n4)
    
    n5=n4
    if len(n4)==0:
        n5 = 'a'
    elif len(n4)>15:
        n5 = n4[:15]
        if n5[-1]=='.':
            n5 = n5[:14]
    #print("n5", n5)
    if len(n5)<=2:
        while len(n5)<3:
            n5 += n5[-1]
    #print("n5",n5)
    answer = n5
    return answer