from collections import defaultdict
def solution(genres, plays):
    answer = []
    hash = defaultdict(int)
    hash2= defaultdict(list)
    #hash3 = defaultdict(int)
    l = len(genres)
    i=0
    for g,p in zip(genres, plays):
        hash[g] += p
        hash2[g].append((i,p))
        #hash3[p] = i
        i+=1
    hash = dict(sorted(hash.items(), key=lambda x:x[1], reverse=True))
    #print(hash)
    #print(hash3)
    
    for k in hash:
        hash2[k].sort(key=lambda x: (-x[1],x[0]))
        #print(hash2[k])
        if len(hash2[k])<=2:
            for i in hash2[k]:
                answer.append(i[0])
        else:
            for i in hash2[k][:2]:
                answer.append(i[0])
        #print(answer)
    return answer