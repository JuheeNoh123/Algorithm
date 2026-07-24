from collections import deque
def solution(begin, target, words):
    answer = 0
    len_words = len(words)
    d = {k:[] for k in words}
    d[begin]=[]
    #print(set(begin), set(words[0]))
    ans=0
    for i in range(len_words):
        ans=0
        for j in range(len(begin)):
            if begin[j]!=words[i][j]:
                ans +=1
        if ans==1:
            d[begin].append(words[i])
            d[words[i]].append(begin)
    ans=0
    for i in range(len_words):
        #d[words[i]]=[]
        for j in range(len_words):
            ans=0
            for k in range(len(begin)):
                if words[i][k]!=words[j][k]:
                    ans +=1
            if ans==1:
                d[words[i]].append(words[j])
    print(d)
    
    q = deque([begin])
    visited={k : False for k in words}
    visited[begin]=False
    def dfs(word,cnt):
        #print(word, visited)
        #print(cnt)
        if target in d[word]:
            return cnt
        visited[word]=True
        for w in d[word]:
            if visited[w] ==False:
                return dfs(w, cnt+1) 
        return 0
    
    
    answer=dfs(begin,1)
        
                
            
        
    return answer