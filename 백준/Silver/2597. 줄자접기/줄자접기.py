import sys
input=sys.stdin.readline

n = int(input())
r1,r2 = map(int, input().split())
b1,b2 = map(int, input().split())
y1,y2 = map(int, input().split())

#print("빨간점 좌표",r1,r2)
mid = (r1+r2)/2
#print("----빨간점 접음----")
if mid<n-mid:
    b1,b2=abs(mid-b1),abs(mid-b2)
    y1,y2=abs(mid-y1),abs(mid-y2)
    n=n-mid
else:
    if b1>mid:
        b1=mid*2-b1
    if b2>mid:
        b2=mid*2-b2
    if y1>mid:
        y1=mid*2-y1
    if y2>mid:
        y2=mid*2-y2
    n=mid
#print("n 줄자 길이 :",n)
#print("파란점 좌표",b1,b2)
#print("노란점 좌표",y1,y2)


if b1!=b2:
    #print("----파란점 접음----")
    mid = (b1+b2)/2
    if mid<n-mid:
        y1,y2=abs(mid-y1),abs(mid-y2)
        n=n-mid
    else:
        if y1>mid:
            y1=mid*2-y1
        if y2>mid:
            y2=mid*2-y2
        n=mid
#else:
    #print("----파란점 접을 필요 없음----")
#print("n 줄자 길이 :",n)
#print("노란점 좌표",y1,y2)

#print("----노란점 접음----")
if y1!=y2:
    mid = (y1+y2)/2
    if mid<n-mid:
        n=n-mid
    else:
        n=mid
print("{:.1f}".format(n))