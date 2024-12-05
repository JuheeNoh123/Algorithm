import sys
input = sys.stdin.readline

n,m = map(int,input().split())

trees = list(map(int,input().split()))

start, end = 1,max(trees)
    
        
while start<=end:
    middle = (start+end)//2
    #print('middle',middle)
    sum=0
    for i in range(n):
        gap = trees[i]-middle
        #print('gap',gap)
        if gap>0:
            sum +=gap
        
    
    #print('res',res)
    if sum>=m:
        start = middle+1
    else:
        end = middle-1
    #print(start,end)
        
    
    

print(end)