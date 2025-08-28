import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = {}

for i in range(N):
    if A[i] not in count:
        count[A[i]] = [0,0]
    count[A[i]][0] += 1

for i in range(N):
    if B[i] not in count:
        count[B[i]] = [0,0]
    count[B[i]][1] +=1
#print(count)
answer = 0
for i in count:
    #print(i)
    answer += min(count[i][0], count[i][1])
print(N-answer)