'''
Andy Shaw
11/3/2014

http://www.reddit.com/r/dailyprogrammer/comments/2l6dll/11032014_challenge_187_easy_a_flagon_of_flags/
'''

if __name__ == '__main__':
    #user enters how many flags to input
    flags = {}
    n = int(raw_input("Enter the number of flags being entered.\n"))

    for i in range(n):
        flag = raw_input('Enter flag {0}: '.format(i))

        short, full = flag.strip().split(':')

        flags[short] = full

    #prompt user
    user = raw_input("> ")

    for e in user.split(' '):
        if e[:2].count('-') == 1:
            for ch in e:
                if ch == '-': 
                    pass
                else:
                    print 'flag: ', flags[ch]
        elif e[:2].count('-') == 2:
            print 'flag: ', e[2:]

        else:
            print 'param:', e