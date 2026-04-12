T = int(input())
F = {}
F[0] = 0
for i in range(1,22):
    if i==1: F[i]=500
    elif 1<i and i<4:
        F[i] = 300
    elif 3<i and i<7:
        F[i] = 200
    elif 6<i and i<11:
        F[i]=50
    elif 10<i and i<16:
        F[i]= 30
    else:
        F[i] = 10
#print(F)
S={}
S[0] = 0
for i in range(1,32):
    if i==1: S[i]=512
    elif 1<i and i<4:
        S[i] = 256
    elif 3<i and i<8:
        S[i] = 128
    elif 7<i and i<16:
        S[i]=64
    else:
        S[i] = 32
#print(S)
for i in range(T):
    sum = 0
    a,b = map(int, input().split())
    p_a=0
    p_b=0
    if F.get(a)!=None:
        p_a = F[a]
    if S.get(b)!=None:
        p_b=S[b]
    
    sum += p_a+p_b
    print(sum*10000)