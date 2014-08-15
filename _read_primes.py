lines = int(open('primes.txt', 'r').readline().strip())

print '1-{0} has been calculated'.format(lines)

import sys

n = int(sys.argv[1])
if not 0 < n <= lines:
    print '{0} has not been calculated'.format(n)
    exit()

f = open('primes.txt', 'r')
line = f.readline() # remove linecount
line = f.readline()
while line:
    if int(line.strip().split(':')[0]) == n:
        print line
        exit()
    line = f.readline()

print '{0} has not been calculated'.format(n)

#print 'longest', lines[index]