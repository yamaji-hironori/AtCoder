import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        n = int(input())

        n_c = n - 1

        ans = 0
        for i_a in range(1, n_c+1):
            max_b = n_c // i_a
            ans += max_b

        print(ans)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)