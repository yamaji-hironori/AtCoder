NumCards = int(input())
SelectCard = int(input())
CardsList = [input() for i in range(NumCards)]

numbers_made_list = []
def select_card(i_select = 1, numbers_made = '', used_card = 0):
    if i_select == SelectCard + 1:
        numbers_made_list.append(numbers_made)
        return
    
    for i_card in range(NumCards):
        if used_card & (1 << i_card) == 0:
            select_card(i_select+1, numbers_made+CardsList[i_card], \
                                                      used_card + (1 << i_card))

    return

select_card()

numbers_made_set = set(numbers_made_list)
print(len(numbers_made_set))