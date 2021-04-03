import sys
sys.setrecursionlimit(10**9)
 
class ABC(object):
 
    def __init__(self):
        pass
 
 
    def main(self):
        r1, c1 = map(int, input().split())
        r2, c2 = map(int, input().split())

        # step0
        if r1 == r2 and c1 == c2:
            print(0)
            return

        # step1
        if r1+c1 == r2+c2 \
            or r1-c1 == r2-c2 \
            or abs(r1-r2)+abs(c1-c2) <= 3:
            print(1)
            return
        
        # step2
        if (r1+c1) % 2 == (r2+c2) % 2:
            print(2)
            return
        elif (r1+c1-3 <= r2+c2 and r2+c2 <= r1+c1+3) \
            or (r1-c1-3 <= r2-c2 and r2-c2 <= r1-c1+3):
            print(2)
            return

        print(3)
        return
 
 
if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)