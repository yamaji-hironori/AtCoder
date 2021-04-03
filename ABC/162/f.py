NumSeq = int(input())
SeqList = list(map(int, input().split()))

if NumSeq % 2 == 0:
    even_sum = sum([SeqList[i] for i in range(NumSeq) if i % 2 == 0])
    odd_sum = sum([SeqList[i] for i in range(NumSeq) if i % 2 == 1])
    print(max(even_sum, odd_sum))
    exit()

left_even = [0] * NumSeq
left_odd = [0] * NumSeq
right_even = [0] * NumSeq
right_odd = [0] * NumSeq

left_even[0] = SeqList[0]
left_odd[1] = SeqList[1]
right_even[NumSeq-1] = SeqList[NumSeq-1]
right_odd[NumSeq-2] = SeqList[NumSeq-2]

for i in range(2, NumSeq):
    if i % 2 == 0:
        left_even[i] = left_even[i-2] + SeqList[i]
        right_even[NumSeq-1-i] = right_even[NumSeq-i+1] + SeqList[NumSeq-1-i]
    else:
        left_odd[i] = left_odd[i-2] + SeqList[i]
        right_odd[NumSeq-1-i] = right_odd[NumSeq-i+1] + SeqList[NumSeq-1-i]


max_sum = max(left_even[-3], left_odd[-2], right_even[2])

for i in range(1, NumSeq - 3):
    if i % 2 == 0:
        max_sum = max(max_sum, left_even[i] + right_odd[i+3], \
                                                 left_even[i] + right_even[i+4])
    else:
        max_sum = max(max_sum, left_odd[i] + right_even[i+3])
        
    if max_sum == 249:
        max_i = i

print(max_sum)