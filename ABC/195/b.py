import sys

def main():
    INF = float('inf')
    a, b, w = map(int, input().split())

    w *= 1000
    max_cnt = INF
    min_cnt = 0
    cnt = 1
    while True:
        w_orenge = w / cnt
        if a <= w_orenge and w_orenge <= b:
            if min_cnt == 0:
                min_cnt = cnt
            max_cnt = cnt
        cnt += 1

        if w_orenge < 1:
            break

    if min_cnt == 0:
        print('UNSATISFIABLE')
    else:
        print('%s %s' %(min_cnt, max_cnt))

    return


if __name__ == '__main__':
    main()
    sys.exit()
