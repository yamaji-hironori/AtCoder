from collections import deque

def main():
    N, M = map(int, input().split())

    table_num = deque()
    if N % 2 == 1:
        for i in range(1, M+1):
            table_num.append('%s %s' % (i, N-i))

    else:
        for i in range(1, M+1):
            if i <= N // 4:
                table_num.append('%s %s' % (i, N+1 - i))

            else:
                table_num.append('%s %s' % (i, N - i))
    
    for i_table in table_num:
        print(i_table)
    
    return

if __name__ == '__main__':
    main()