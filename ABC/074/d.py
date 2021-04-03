import sys
sys.setrecursionlimit(10**9)
import heapq

def main():
    n = int(input())
    a = list(map(int, input().split()))

    one_third = a[0:n]
    three_third = [-x for x in a[2*n:3*n]]
    heapq.heapify(one_third)
    heapq.heapify(three_third)

    one_sum = [0]*(n+1)
    one_sum[0] = sum(one_third)
    three_sum = [0]*(n+2)
    three_sum[n+1] = -sum(three_third)
    for i in range(n, 2*n):
        two_num_for_one = a[i]
        min_num = heapq.heappushpop(one_third, two_num_for_one)
        one_sum[i-n+1] = one_sum[i-n] - min_num + two_num_for_one

        two_num_for_three = -a[3*n-i-1]
        max_num = -heapq.heappushpop(three_third, two_num_for_three)
        three_sum[2*n-i] = three_sum[2*n-i+1] - max_num - two_num_for_three

    score = -float('inf')
    for i in range(n+1):
        score = max(score, one_sum[i]-three_sum[i+1])

    print(score)        
    return


if __name__ == "__main__":
    main()
    sys.exit(0)