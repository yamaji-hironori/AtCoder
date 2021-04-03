import sys
sys.setrecursionlimit(10**9)

class AtCoder(object):
    def __init__(self):
        pass

    def main(self):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        ans = a*d - c*b
        print(ans)
        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
