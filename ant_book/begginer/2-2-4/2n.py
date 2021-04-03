NumPoints = int(input())
RedPoints = [[int(_) for _ in input().split()] for i in range(NumPoints)]
BluePoints = [[int(_) for _ in input().split()] for i in range(NumPoints)]

RedPoints.sort(key=lambda x: (-x[0], -x[1]))
BluePoints.sort(key=lambda x: (-x[0], -x[1]))

establish_pair = 0

def find_pair():
    global establish_pair
    for i_blue_y, i_blue_x in BluePoints:
        count_pair = 0
        for i_red_y, i_red_x in RedPoints:
            if i_red_y < i_blue_y and i_red_x < i_blue_x:
                count_pair += 1
                candidate_y, candidate_x = i_red_y, i_red_x

        if count_pair != 1:
            continue
        establish_pair += 1
        BluePoints.remove([i_blue_y, i_blue_x])
        RedPoints.remove([candidate_y, candidate_x])
        return
    
    else:
        for i_blue_y, i_blue_x in BluePoints:
            for i_red_y, i_red_x in RedPoints:
                if i_red_y < i_blue_y and i_red_x < i_blue_x:
                    establish_pair += 1
                    BluePoints.remove([i_blue_y, i_blue_x])
                    RedPoints.remove([i_red_y, i_red_x])
                    return
    return

while len(BluePoints) > 0:
    pre_establish_pair = establish_pair
    find_pair()

    if pre_establish_pair == establish_pair:
        break

print(establish_pair)