import queue

K = int(input())

que_lunlun = queue.Queue()
for i in range(1, 10):
    que_lunlun.put(i)

for _ in range(K):
    now_lunlun = que_lunlun.get()
    
    first_digit = now_lunlun % 10
    if first_digit != 0:
        que_lunlun.put(now_lunlun*10 + first_digit-1)
    
    que_lunlun.put(now_lunlun*10 + first_digit)

    if first_digit != 9:
        que_lunlun.put(now_lunlun*10 + first_digit+1)
    
print(now_lunlun)