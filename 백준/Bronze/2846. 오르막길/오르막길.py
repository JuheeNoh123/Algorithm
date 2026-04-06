S = int(input())
L= list(map(int,input().split()))
A = [0 for _ in range(S)]
cnt = 0
up = 0
for i in range(S-1):
    if L[i]<L[i+1]:
        #print(L[i])
        A[i+1]=A[i] + (L[i+1]-L[i])

print(max(A))