ax,ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
L=[(ax,ay),(bx,by),(cx,cy)]

L.sort()

can=1
if ax==bx and bx==cx:
    can=0
elif ay==by and by==cy:
    can=0
else:
    ab_x = L[1][0]-L[0][0]
    ab_y = L[1][1]-L[0][1]
    
    bc_x = L[2][0]-L[1][0]
    bc_y = L[2][1]-L[1][1]
    #print(ab_x,ab_y,bc_x,bc_y )
    if ab_x!=0 and bc_x!=0:
        if ab_y/ab_x == bc_y/bc_x:
            can = 0

if can==0:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")


