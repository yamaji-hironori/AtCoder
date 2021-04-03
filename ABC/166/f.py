import sys
from collections import deque

def main():
    N, A, B, C = map(int, input().split())
    s_list = [input() for i in range(N)]

    select_list = deque()
    select_list.append('Yes')
    for i, i_s in enumerate(s_list):
        if i_s == 'AB':
            if A == 0 and B == 0:
                select_list = ['No']
                break
            elif A > B:
                A -= 1
                B += 1
                select_list.append('B')
            else:
                A += 1
                B -= 1
                select_list.append('A')
        elif i_s == 'AC':
            if A == 0 and C == 0:
                select_list = ['No']
                break
            elif A > C:
                A -= 1
                C += 1
                select_list.append('C')
            else:
                A += 1
                C -= 1
                select_list.append('A')
        else:
            if B == 0 and C == 0:
                select_list = ['No']
                break
            elif B > C:
                B -= 1
                C += 1
                select_list.append('C')
            else:
                B += 1
                C -= 1
                select_list.append('B')

    for i in select_list:
        print(i)

    return

if __name__ == '__main__':
    main()
    sys.exit(0)