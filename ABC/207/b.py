import math

def main():
    a, b, c, d = map(int, input().split())
    if b < (c * d):
        ans = math.ceil(a / (d*c -b))
    elif b >= (c * d):
        ans = -1
    else:
        raise
    print(ans)

if __name__ == "__main__":
    main()
