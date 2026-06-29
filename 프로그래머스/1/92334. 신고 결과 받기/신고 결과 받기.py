def solution(id_list, report, k):
    answer = [0]*len(id_list)
    name = {}
    rep_board = {}
    for i in id_list:
        name[i]=[]
        rep_board[i]=[]
    for r in report:
        id, rp = r.split()
        name[id].append(rp)
        name[id]=list(set(name[id]))
        rep_board[rp].append(id)
        rep_board[rp] = list(set(rep_board[rp]))
    #print(name)
    #print(rep_board)
    rep = []
    for rp_id in rep_board:
        if len(rep_board[rp_id])>=k:
            idx=0
            for n in name:
                if rp_id in name[n]:
                    answer[idx]+=1
                idx+=1
        
    return answer