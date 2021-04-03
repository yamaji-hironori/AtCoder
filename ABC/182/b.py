import sys
sys.setrecursionlimit(10**9)

class AtCoder(object):
    def __init__(self):
        pass

    def main(self):
        N = int(input())
        A = list(map(int, input().split()))

        # index '0' is not used.
        cnt = [0 for _ in range(1001)]
        for i in range(2, 1001):
            for i_A in A:
                if i_A % i == 0:
                    cnt[i] += 1

        max_cnt = max(cnt)
        ans = cnt.index(max_cnt)
        print(ans)
        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
