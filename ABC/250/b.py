import sys
sys.setrecursionlimit(10**9)


def main():
    N, A, B = map(int, input().split())

    S = []
    # 縦N回
    for i_tate_N in range(N):
        # 縦A回
        for _ in range(A):
            now_S = ""
            # 横N回
            for i_yoko_N in range(N):
                if (i_tate_N % 2) == 0:
                    if (i_yoko_N % 2) == 0:
                        now_S += "."*B
                    else:
                        now_S += "#"*B
                else:
                    if (i_yoko_N % 2) == 0:
                        now_S += "#"*B
                    else:
                        now_S += "."*B
            S.append(now_S)

    for i_S in S:
        print(i_S)
    return


if __name__ == "__main__":
    main()
