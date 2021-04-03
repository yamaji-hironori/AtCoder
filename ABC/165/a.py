def main():
    K = int(input())
    A, B = map(int, input().split())

    for i in range(A, B+1):
        if i % K == 0:
            ans = 'OK'
            break
    else:
        ans = 'NG'

    print(ans)

if __name__ == '__main__':
    main()