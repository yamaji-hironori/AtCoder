import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        N = int(input())
        AB = [[int(_) for _ in input().split()] for i in range(N)]

        ans = 0
        for a, b in AB:
            ans += ((a+b)*(b-a+1))//2

        print(ans)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)