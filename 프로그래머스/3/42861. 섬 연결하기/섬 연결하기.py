def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parents=list(range(n))
    def find(x):
        if parents[x]!=x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(a,b):
        rx = find(a)
        ry = find(b)
        if rx!=ry:
            parents[rx] = ry
    
    for a,b,x in costs:
        if find(a) != find(b):
            union(a,b)
            answer += x
    return answer