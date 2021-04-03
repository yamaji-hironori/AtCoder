"""
1.都市１から各都市まで移動する。
2.各都市から都市１以外に移動する。
3.2で各都市についた時間が1の時間より早ければ時間を更新し、2を再度実行する。
4.3が全て終わった時の時間が答えとなるはず
"""
import math
from collections import deque

N, M, S = map(int, input().split())

city_tree = [[] for _ in range(N)]
for _ in range(M):
    u, v, a, b = map(int, input().split())
    city_tree[u-1].append([v-1, a, b])
    city_tree[v-1].append([u-1, a, b])

C_D_list = [[int(_) for _ in input().split()] for i in range(N)]

def get_arrival_time(start_city, goal_city, start_time, silver_coin):
    min_arrival_time = None
    pass_city_deque = deque()
    passed_binary = 0
    for i_city in city_tree[start_city]:
        next_city, total_cost, total_time = i_city
        passed_binary = 1 << next_city
        pass_city_deque.append([next_city,total_cost,total_time,passed_binary])

    while len(pass_city_deque) > 0:
        now_city,total_cost,total_time,passed_binary=pass_city_deque.popleft()

        if now_city == goal_city:
            now_silver_coin = silver_coin - total_cost
            exchange_coin, exchange_time = C_D_list[start_city]
            exchange_num = math.ceil((total_cost - silver_coin) / exchange_coin)
            if exchange_num > 0:
                total_time += exchange_time * exchange_num
                now_silver_coin += exchange_coin * exchange_num

            if min_arrival_time is None:
                min_arrival_time = total_time + start_time
            else:
                min_arrival_time = min(min_arrival_time, total_time+start_time)
            continue

        for i_city in city_tree[now_city]:
            next_city, next_cost, next_time = i_city
            if passed_binary & (1 << next_city):
                continue

            next_total_cost = total_cost + next_cost
            next_total_time = total_time + next_time
            next_passed_binary = passed_binary + (1 << next_city)
            pass_city_deque.append( \
              [next_city, next_total_cost, next_total_time, next_passed_binary])
    return min_arrival_time, now_silver_coin

arrival_time_coin = [-1] * N
arrival_time_coin[0] = [0, 0]
start_city, start_time = 0, 0
for i_goal_city in range(1, N):
    arrival_time_coin[i_goal_city] = \
                  list(get_arrival_time(start_city, i_goal_city, start_time, S))

start_goal_deque = deque()
for i_start_city in range(1, N):
    for j_goal_city in range(1, N):
        if i_start_city == j_goal_city:
            continue
        
        now_time, now_coin = arrival_time_coin[i_start_city]
        start_goal_deque.append([i_start_city, j_goal_city, now_time, now_coin])

while len(start_goal_deque) > 0:
    start_city, goal_city, now_time, now_coin = start_goal_deque.popleft()
    arrival_time, arrival_coin = \
                     get_arrival_time(start_city, goal_city, now_time, now_coin)

    if arrival_time_coin[goal_city][0] > arrival_time:
        arrival_time_coin[goal_city] = [arrival_time, arrival_coin]
        for next_goal_city in range(1, N):
            if goal_city == next_goal_city:
                continue
            start_goal_deque.append( \
                        [goal_city, next_goal_city, arrival_time, arrival_coin])

for i_time, _ in arrival_time_coin[1:]:
    print(i_time)