import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        a, b = map(int, input().split())
        s = input()
        point = b
        for i_s in s:
            if i_s == 'o':
                point += 1
            elif point > 0:
                point -= 1
            
        print(point)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)