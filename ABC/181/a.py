import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        N = int(input())
        if N % 2 == 0:
            print('White')
        else:
            print('Black')
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)