S = input()
T = input()
N = len(S)
K = len(T)
A = list(S)
for i in range(N-K,-1,-1):
    a = S[i:i+K]

    flag = 0
    for j in range(K):
        if a[j]!="?" and a[j]!=T[j]:
            flag = 1
            break

    if flag==1:
        continue

    A[i:i+K] = T[:]
    for j in range(N):
        if A[j]=="?":
            A[j]="a"
    break

if "?" in A:
    print("UNRESTORABLE")
else:
    print("".join(A))
