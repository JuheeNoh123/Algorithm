def solution(board, moves):
    answer = 0
    stack =[]
    for i in moves:
        #print(stack)
        pos = 0
        while pos<len(board):
            #print(board[pos][i-1])
            if not board[pos][i-1]:
                pos +=1
            else:
                if len(stack):
                    if stack[-1]==board[pos][i-1]:
                        stack.pop()
                        #print("===", stack)
                        board[pos][i-1]=0
                        answer+=2
                        break
                stack.append(board[pos][i-1]) 
                board[pos][i-1]=0
                #print('---',stack)
                break
    return answer