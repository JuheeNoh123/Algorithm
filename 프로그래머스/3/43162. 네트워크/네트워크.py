from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if visited[i]==False:
            answer+=1
            #print(i)
            q = deque([i])
            visited[i]=True
            while q:
                #print(q)
                #print(visited)
                num = q.popleft()
                for j in range(n):
                    #print(j, visited)
                    if visited[j]==False and computers[num][j]==1:
                        q.append(j)
                        visited[j]=True
                
    return answer