NumSeq, MaxNum = map(int, input().split())
mod = 10**9 + 7

# List containing the number of sequences for each greatest common divisor.
num_sequence_list = [0] * (MaxNum + 1)

total_value = 0
for i_divisor in range(MaxNum, 0, -1):
    num_sequence = pow(MaxNum//i_divisor, NumSeq, mod)

    for j_multiple in range(2, MaxNum//i_divisor+1):
        num_sequence -= num_sequence_list[i_divisor*j_multiple]

    num_sequence_list[i_divisor] = num_sequence
    total_value += num_sequence * i_divisor

print(total_value % mod)