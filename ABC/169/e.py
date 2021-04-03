import sys
import copy

def odd(N, AB):
    ans = []
    AB.sort()
    half = []
    for _, i_B in AB[(N+1)//2-1:]:
        half.append(i_B) 
    min_b = min(half)
    for i in range(AB[(N+1)//2-1][0], min_b+1):
        ans.append(i)

    AB.sort(key=lambda  x: x[1], reverse=True)
    half = []
    for i_A, _ in AB[(N+1)//2-1:]:
        half.append(i_A)
    max_a = max(half)
    for i in range(max_a, AB[(N+1)//2-1][1]+1):
        ans.append(i)

    ans = set(ans)
    ans = len(ans)
    return ans

def even(N, AB):
    ans = []
    AB.sort()
    half = []
    for _, i_B in AB[N//2-1:]:
        half.append(i_B) 
    min_b = min(half)
    start = (AB[N//2-1][0] + AB[N//2][0])//2
    if (AB[N//2-1][0] + AB[N//2][0]) % 2 == 1:
        ans.append(start+0.5)
        start += 1
    for i in range(start, min_b+1):
        ans.append(i)
        ans.append(i+0.5)

    AB.sort(key=lambda  x: x[1], reverse=True)
    half = []
    for i_A, _ in AB[N//2-1:]:
        half.append(i_A)
    max_a = max(half)
    end = (AB[N//2-1][1] + AB[N//2][1])//2
    for i in range(max_a, end):
        ans.append(i)
        ans.append(i+0.5)
    else:
        if max_a == end:
            i = max_a
        if (AB[N//2-1][1] + AB[N//2][1]) % 2 == 0:
            ans.append(i+1)

    ans = set(ans)
    ans = len(ans)
    return ans

def main():
    N = int(input())
    AB = [[int(_) for _ in input().split()] for i in range(N)]

    if N % 2 == 0:
        ans = even(N, AB)
    else:
        ans = odd(N, AB)
    
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)