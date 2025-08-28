import sys
input = sys.stdin.readline


N = int(input())
for i in range(N):
    A,B = map(int, input().split())
    A_list = [A]
    B_list = [B]
    while True:
        A//=2
        A_list.append(A)
        B//=2
        B_list.append(B)
        if A in B_list:
            print(A*10)
            break
        elif B in A_list:
            print(B*10)
            break
        

    