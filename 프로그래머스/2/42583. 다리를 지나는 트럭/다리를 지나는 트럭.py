from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    b = deque([0]*bridge_length)
    t = deque(truck_weights)
    time=0
    c_w=0
    while t:
        time+=1
        c_w -= b.popleft()
        
        if c_w+t[0]<=weight:
            b.append(t[0])
            c_w+=t[0]
            t.popleft()
        else:
            b.append(0)
            
    return time+bridge_length