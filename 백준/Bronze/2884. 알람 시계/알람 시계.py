H, M = map(int, input().split())
a = M-45  
if a>=0:
    print(H,a)
else:   
    h=H-1
    if h>=0:
        print(h, 60+a)
    else:
        print(24+h,60+a) 