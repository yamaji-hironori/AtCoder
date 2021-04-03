import math

def main():
    X = int(input())

    ans = 0
    interest = 100
    while True:
        if X <= interest:
            break

        interest = math.floor(interest*1.01)
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()