def main():
    import math

    K = int(input())

    total_ans = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
                total_ans += math.gcd(i, math.gcd(j, k))

    print(total_ans)

if __name__ == '__main__':
    main()