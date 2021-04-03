import sys
sys.setrecursionlimit(10**9)

class AtCoder(object):
    def __init__(self):
        pass

    def main(self):
        A, B = map(int, input().split())
        ans = (2*A+100) - B
        print(ans)
        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
