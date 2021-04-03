import sys

def main():
    S = input()
    S_list = [S[i] for i in range(0, 4)]

    S_set = set(S_list)
    if len(S_set) != 2:
        print('No')
        return
    
    for i_set in S_set:
        num = 0
        for i_list in S_list:
            if i_set == i_list:
                num += 1
        
        if num != 2:
            print('No')
            break
    
    else:
        print('Yes')
        
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
