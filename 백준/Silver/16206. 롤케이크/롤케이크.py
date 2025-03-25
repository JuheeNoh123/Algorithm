import sys
input = sys.stdin.readline
N, M = map(int, input().split())

L = list(map(int, input().split()))

L.sort(key=lambda x:(x%10,x))
#print(L)
#cnt=0
# for i in range(N):
#     if M-L[i]//10>=0:
#         M-=L[i]//10
#         if L[i]%10==0:
#             M+=1
    
#         cnt+=L[i]//10
#     else:
#         if M*10<L[i]:
#             cnt+=M
#             if (M+1)*10==L[i]:
#                 cnt+=1
#             M=0
# print(cnt)

cut = 0
cnt=0
for i in range(N):
    if L[i]%10==0:
        cut=L[i]//10-1
        if cut>M:#딱 나누어 떨어져서 잘라지지 않는경우
            cnt+=M
        else:
            cnt+=(cut+1)
    
    else:
        cut=L[i]//10
        if cut>M:
            cnt+=M
        else:
            cnt+=cut
            
    M-=cut
    if M<=0:
        break
print(cnt)