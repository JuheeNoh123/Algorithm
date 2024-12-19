import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
L=[s[0]]
visited=[0]*n
visited[0]=1
for i in range(1,n):
    #print(s[i])
    if s[i]==')':
        if len(L)>0 and L[-1]=='(':
            L.pop()
        else:
            if visited[len(L)]==0:
                visited[len(L)]=1
            L.append(')')
    else:   #(
        if len(L)>0 and L[-1]==')':
            L.pop()
        else:
            #print(len(L))
            if visited[len(L)]==0:
                visited[len(L)]=1
            L.append('(')
    # print(L)
    # print(visited)
if len(L)==0:
    print(sum(visited))
else:
    print(-1)