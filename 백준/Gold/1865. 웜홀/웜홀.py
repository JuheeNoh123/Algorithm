import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())


def bf():
    for i in range(N):
        #print("---------------",i)
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            #print(cur, next, cost)
            if dist[next]>dist[cur]+cost: #다음 노드로 이동하는 거리가 현재 경우에 더 짦은 경우
                dist[next]=dist[cur]+cost
                #print(dist)
                if i==N-1: #음의 간선 사이클이 존재하는지 여부만 알면 됨
                    return True
    return False


for _ in range(N):
    edges=[]
    N,S,W = map(int, input().split())
    dist = [INF]*(N+1)
    for i in range(S):
        s,e,t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    
    for i in range(W):
        s,e,t = map(int, input().split())
        edges.append((s,e,-t))

    if bf():
        print("YES")
    else:
        print("NO")
    