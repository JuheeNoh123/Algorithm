def solution(sizes):
    answer = 0
    w = []
    h = []
    s = len(sizes)
    for i in range(s):
        sizes[i].sort()
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    answer = max(w)*max(h)
    return answer