import sys

def main():
    N, M, Q = map(int, input().split())
    S = [[int(_) for _ in input().split()] for i in range(Q)]

    # index '0' is not using
    is_pass = [[False]*(M+1) for _ in range(N+1)]
    problem_score = [N]*(M+1)

    for i_s in S:
        if i_s[0] == 1:
            participant = i_s[1]
            score = 0
            for i, i_problem in enumerate(is_pass[participant]):
                if i_problem == True:
                    score += problem_score[i]
            print(score)

        else:
            participant = i_s[1]
            problem = i_s[2]
            is_pass[participant][problem] = True
            problem_score[problem] -= 1

    return


if __name__ == "__main__":
    main()
    sys.exit(0)