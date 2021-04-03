import sys
sys.setrecursionlimit(10**9)

class AtCoder(object):
    def __init__(self):
        pass

    def main(self):
        N = input()
        digit = len(N)

        # index '0' is not used.
        cnt_bi_appearance = [0 for _ in range(163)]
        for i_N in N:
            i_N = int(i_N)

            for i in range(162, 0, -1):
                if cnt_bi_appearance[i] != 0:
                    now = cnt_bi_appearance[i+i_N]
                    if now < (cnt_bi_appearance[i] + 1):
                        cnt_bi_appearance[i+i_N] = cnt_bi_appearance[i] + 1

            if cnt_bi_appearance[i_N] == 0:
                cnt_bi_appearance[i_N] = 1

        max_digit = 0
        for i in range(1, 163):
            if cnt_bi_appearance[i] != 0 \
                    and i % 3 == 0 \
                    and max_digit < cnt_bi_appearance[i]:
                max_digit = cnt_bi_appearance[i]

        if max_digit == 0:
            print(-1)
            exit()

        ans = digit - max_digit
        print(ans)

        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
