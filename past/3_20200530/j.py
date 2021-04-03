import sys
import bisect

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # index '0' is not using.
    # Consider in descending order for the sake of 'bisect'.
    children = [0]*(N+1)
    children[0] = -float('inf')

    for i_A in A:
        insert_index = bisect.bisect_left(children, i_A)
        if insert_index == 1:
            print(-1)
            continue

        children[insert_index-1] = i_A
        print(N+1 - insert_index + 1)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)