import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        n = int(input())
        dd = [[int(_) for _ in input().split()] for i in range(n)]

        cnt = 0
        for d1, d2 in dd:
            if d1 == d2:
                cnt += 1
            else:
                cnt = 0

            if cnt >= 3:
                print('Yes')
                break
        else:
            print('No')

        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)