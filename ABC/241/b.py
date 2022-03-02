import sys
sys.setrecursionlimit(10**9)

class ABC:

    def __init__(self):
        pass

    def main(self):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        for b in B:
            try:
                A.remove(b)
            except Exception:
                print("No")
                break
        else:
            print("Yes")


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)
