import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        N = int(input())
        XY = [[int(_) for _ in input().split()] for i in range(N)]

        for i in range(N):
            for j in range(i+1,N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                dy = y2-y1
                dx = x2-x1

                for k in range(j+1,N):
                    x3, y3 = XY[k]

                    if dx * (y3-y1) == dy * (x3-x1):
                        print('Yes')
                        return
        else:
            print('No')

        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)