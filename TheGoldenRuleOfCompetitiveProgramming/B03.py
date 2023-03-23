
def main():
    _ = int(input())
    A_list = [int(_) for _ in input().split()]

    for i in range(len(A_list)):
        for j in range(i+1, len(A_list)):
            for k in range(j+1, len(A_list)):
                if (A_list[i]+A_list[j]+A_list[k]) == 1000:
                    print('Yes')
                    return
    else:
        print('No')

main()
