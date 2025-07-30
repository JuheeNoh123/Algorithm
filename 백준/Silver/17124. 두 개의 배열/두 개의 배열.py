import sys
input = sys.stdin.readline
'''
20 5 14 9
16 8 12

8 12 16 -> m=8

'''
def b(L,s,e,t):
    
    m = (s+e)//2
    #print(s,e,m)
    if(s>=len(L)):
        return L[-1]
    if(e<0):
        return L[0]
    
    if s<=e:
        if t<L[m]:
            return b(L,s,m-1,t)
        elif t>L[m]:
            return b(L,m+1,e,t)
        else:
            return L[m]
    else:
        e_t_gap = t-L[e]
        t_s_gap = L[s]-t
        #print(e_t_gap)
        #print(t_s_gap)
        if e_t_gap <= t_s_gap:
            #print("반환값 :" ,L[e])
            return L[e]
        else:
            #print("반환값 :",L[s])
            return L[s]
        

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    B.sort()
    #print(B)
    s=0
    for i in A:
        #print("찾는 숫자 : ",i)
        v = b(B,0,m-1,i)
        s+=v
    print(s)