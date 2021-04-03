import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    # index '0' is not used.
    fact = [2]*(n+1)
    fact[1] = 1

    for i in range(2, n+1):
        if n < i*i:
            break
        else:
            fact[i*i] += 1

        for j in range(i+1, n+1):
            now = i*j
            if now <= n:
                fact[i*j] += 2
            else:
                break
    
    ans = 0
    for i in range(1, n+1):
        ans += i * fact[i]

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)