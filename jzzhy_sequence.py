'''
Andy Shaw
8/6/2014

from http://codeforces.com/contest/450/problem/B
'''

def new_fib(x, y, n):
    n = n%6
    #pattern repeats itself every 6 places of the sequence
    if n == 1:
        return x
    elif n == 2:
        return y
    elif n == 3:
        return y-x
    elif n == 4:
        return -x
    elif n == 5:
        return -y
    elif n == 0:
        return -(y-x)

def main(x, y, n):
    return new_fib(x, y, n) % 1000000007

if __name__ == '__main__':
    import sys
    import os
    import time

    x = 0
    y = 0
    n = 0

    args = sys.argv[1:]
    try:
        if len(args) == 3:
            x = int(args[0])
            y = int(args[1])
            n = int(args[2])
        else:
            raise
    except:
        print 'USAGE: python test.py x y n'
        exit()

    print 'input:'
    print x, y
    print n
    print '--------------------------'
    print 'output:'
    print main(x, y, n)