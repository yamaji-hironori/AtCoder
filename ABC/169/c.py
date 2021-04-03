import sys
import math

def main():
    a, b = input().split()
    a = int(a)
    b = float(b)

    ans = math.floor(a*b)
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)