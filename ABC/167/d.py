import sys

def main():
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list = [x-1 for x in A_list]

    passed_list = [False] * N
    time_go_same_city = 0
    now_city = 0
    passed_list[now_city] = True
    while True:
        next_city = A_list[now_city]
        if passed_list[next_city]:
            start_circle_city = next_city
            break
        passed_list[next_city] = True
        time_go_same_city += 1
        now_city = next_city

    passed_list = [False] * N
    time_circle_city = 1
    now_city = start_circle_city
    passed_list[now_city] = True
    while True:
        next_city = A_list[now_city]
        if passed_list[next_city]:
            break
        passed_list[next_city] = True
        time_circle_city += 1
        now_city = next_city

    if time_go_same_city >= K:
        num_teleport = 0
        now_city = 0
        while num_teleport < K:
            next_city = A_list[now_city]
            num_teleport += 1
            now_city = next_city
        print(now_city+1)
        return
    
    K -= time_go_same_city
    K %= time_circle_city
    if K == 0:
        K = time_circle_city
    num_teleport = 1
    now_city = start_circle_city
    while num_teleport < K:
        next_city = A_list[now_city]
        num_teleport += 1
        now_city = next_city

    print(now_city+1)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)