import queue
q = queue.Queue()
for i in range(1,10):
    q.put(i)
K = int(input())
for k in range(K):
    x =q.get()
    last = x % 10
    if last != 0:
        q.put(10*x + last - 1)
    q.put(10*x + last)
    if last != 9:
        q.put(10*x + last + 1)
print (x)
