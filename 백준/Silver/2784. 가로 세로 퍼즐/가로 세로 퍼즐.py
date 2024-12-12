from itertools import combinations, permutations

w = [input().strip() for _ in range(6)]

def transfer(L):
    res = ['']*3
    for i in range(3):
        for j in range(3):
            res[j] += L[i][j]
    return res
ans = 'zzzzzzzzzzzzzzz'
for num in combinations(range(6),3):  #6개중에 고를 단어 3개 선택
    words = [w[i] for i in num]
    other_num = set(range(6))-set(num)
    others = [w[i] for i in other_num]
    others.sort()
    for o in permutations(range(3),3):  #words의 세개의 단어를 놓을 수 있는 방법의 수
        transfer_word = [words[j] for j in o]
        t_word = transfer(transfer_word)
        t_word.sort()
        if t_word == others:
            transfer_word = ''.join(transfer_word)
            if ans > transfer_word:
                ans = transfer_word

if ans != 'zzzzzzzzzzzzzzz':
    for i in range(3):  #정답 모양으로 출력
        print(ans[i*3:i*3+3])
else:
    print(0)