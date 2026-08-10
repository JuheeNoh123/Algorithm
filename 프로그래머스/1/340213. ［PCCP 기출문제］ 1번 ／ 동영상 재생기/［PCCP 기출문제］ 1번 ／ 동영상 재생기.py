def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    m,s = map(int, pos.split(':'))
    op_start_m, op_start_s = map(int, op_start.split(':'))
    op_end_m, op_end_s = map(int, op_end.split(':'))
    video_len_m, video_len_s = map(int, video_len.split(':'))
    pos=m*60+s
    op_start = op_start_m*60 + op_start_s
    op_end = op_end_m*60+op_end_s
    video_len = video_len_m*60+video_len_s
    #print(pos, op_start, op_end, video_len)
    if op_start <= pos <= op_end:
        pos=op_end
    for command in commands:
        if command =='next':
            pos+=10
            if op_start <= pos <= op_end:
                pos=op_end
            if pos>video_len:
                pos=video_len
        else:
            pos -= 10
            if pos<0:
                pos=0
            if op_start <= pos <= op_end:
                pos=op_end
            
    min = pos//60
    sec = pos%60
    if min < 10:
        a='0'+str(min)
    else:
        a = str(min)
    if sec<10:
        b='0'+str(sec)
    else:
        b = str(sec)
    answer=a+':'+b
    return answer