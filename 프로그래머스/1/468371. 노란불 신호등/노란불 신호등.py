def solution(signals):
    answer = -1
    rgb = [0 for _ in range(3000000)]
    for signal in signals:
        idx = signal[0]+1
        while idx<2000000:
            for i in range(idx, idx+signal[1]):
                rgb[i]+=1
                if rgb[i]==len(signals):
                    return i
            idx+=signal[1]+signal[2]+signal[0]
            
    #print(rgb)    
    return answer
