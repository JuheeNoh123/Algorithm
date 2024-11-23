import sys
input = sys.stdin.readline

n = int(input())
std = list(map(int, input().split()))

# 정렬
std.sort()
#print(std)
left = [0]*n
for i in range(1,n,2):
    left[i] = left[i-2] + std[i]-std[i-1]
    
right = [0]*(n+2)
for i in range(n-1,1,-2):
    right[i] = right[i+2] + std[i]-std[i-1]
#print(left,right)

min_awk = 10**10
for i in range(0,n-1,2):
    awk3 = std[i+2]-std[i]
    awk2_left = left[i-1] if i>0 else 0
    awk2_right = right[i+4] if i+2 < n-1 else 0
    #print(awk3,awk2_left,awk2_right )
    min_awk = min(min_awk, awk3+awk2_left+awk2_right)
print(min_awk)