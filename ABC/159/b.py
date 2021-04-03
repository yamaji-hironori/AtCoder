S = input()
N = len(S)

if N == 3:
    if S[0] == S[2]:
        print('Yes')
    else:
        print('No')
    exit()

def is_circular(string):
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False

if is_circular(S) and is_circular(S[:(N)//2]) and is_circular(S[(N+3)//2]):
    print('Yes')
else:
    print('No')