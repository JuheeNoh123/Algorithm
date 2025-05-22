import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

newL = []

for i in range(N):
    dic = {}
    row = []
    for j in range(M):
        if L[i][j] not in dic:
            dic[L[i][j]] = j + 1
        row.append((L[i][j], dic[L[i][j]]))
    row.sort()
    newL.append(''.join(map(str, (val[1] for val in row))))

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if newL[i] == newL[j]:
            cnt += 1

print(cnt)
