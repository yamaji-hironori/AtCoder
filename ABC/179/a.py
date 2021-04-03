import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        s = input()
        
        if s[-1] == 's':
            s += 'es'
        else:
            s += 's'
        
        print(s)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)