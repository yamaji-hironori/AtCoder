import sys
sys.setrecursionlimit(10**9)

class ABC:

    def __init__(self):
        pass

    def main(self):
        a_list = list(map(int, input().split()))
        i = 0
        for _ in range(3):
            i = a_list[i]

        print(i)


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)
