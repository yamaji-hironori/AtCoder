import queue

q_lunlun_num = queue.Queue()
for i in range(1, 10):
    q_lunlun_num.put(i)

K = int(input())
for _ in range(K):
    now_lunlun_num = q_lunlun_num.get()
    first_digit = now_lunlun_num % 10

    if first_digit != 0:
        q_lunlun_num.put(now_lunlun_num*10 + first_digit - 1)
    
    q_lunlun_num.put(now_lunlun_num*10 + first_digit)

    if first_digit != 9:
        q_lunlun_num.put(now_lunlun_num*10 + first_digit + 1)

print(now_lunlun_num)