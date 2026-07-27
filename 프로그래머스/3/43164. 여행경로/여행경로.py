
def solution(tickets):
    answer = []
    graph = {}
    for a,b in tickets:
        graph.setdefault(a,[]).append([b,False])
    for v in graph.values():
        v.sort()
    
    n=len(tickets)
    
    def dfs(here, path):
        if len(path)==n+1:
            answer.extend(path)
            return True
        
        for ticket in graph.get(here, []):
            dest, used=ticket
            if not used:
                ticket[1]=True
                if dfs(dest, path+[dest]):
                    return True
                ticket[1] = False
        return False
    
    dfs("ICN", ["ICN"])
    
    return answer