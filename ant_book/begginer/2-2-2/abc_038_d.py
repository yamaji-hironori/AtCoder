import bisect

NumGift = int(input())
ListWidthHeight = [[int(_) for _ in input().split()] for i in range(NumGift)]

ListWidthHeight.sort(key=lambda x: (x[0],-x[1]))

box_height_dp = [10**5]*NumGift
max_box_element = 0

for _, i_height in ListWidthHeight:
    now_box_position = bisect.bisect_left(box_height_dp, i_height)
    box_height_dp[now_box_position] = i_height
    max_box_element = max(max_box_element, now_box_position)

max_box_num = max_box_element + 1
print(max_box_num)