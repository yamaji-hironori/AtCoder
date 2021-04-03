import sys

def main():
    N, M = map(int, input().split())
    H_list = list(map(int, input().split()))
    AB_list = [[int(_) for _ in input().split()] for i in range(M)]

    tree = [[] for _ in range(N)]

    for a, b in AB_list:
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    good_observatory = 0

    for i_obs in range(N):
        if len(tree[i_obs]) == 0:
            good_observatory += 1
            continue

        now_height = H_list[i_obs]
        good_flag = True
        for i_tree in tree[i_obs]:
            if now_height <= H_list[i_tree]:
                good_flag = False
        if good_flag:
            good_observatory += 1

    print(good_observatory)
    return


    if a:
        print('Yes')
    else:
        print('No')

    return

if __name__ == '__main__':
    main()
    sys.exit(0)