K = int(input())

order = 0
digit = 1

def recursion(now_digit, now_num):
    if now_digit == 1:
        return 1

    lunlun_amount = 0
    if now_num != 9:
        lunlun_amount += recursion(now_digit-1, now_num+1)

    lunlun_amount += recursion(now_digit-1, now_num)

    if now_num != 0:
        lunlun_amount += recursion(now_digit-1, now_num-1)

    return lunlun_amount

while order < K:
    for i in range(1, 10):
        order += recursion(digit, i)

print(order)


