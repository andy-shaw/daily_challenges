import prime_factor_trees as p
import sys

longest_num_len = 6 #to ljust number when printed to string

args = sys.argv[1:]
if len(args) < 1:
    n = 5000000001
else:
    n = int(sys.argv[1]) + 1

lines = ''

open('primes.txt', 'w').write(str(n-1) + '\n')

print 'Will write to file every 5000 numbers regardless of what is being printed to console.'

i = 1
while i < n:

    if i%(n/20) == 0: 
        print i, 'is complete'

    if i%5000 == 0:
        open('primes.txt', 'a').write(lines)
        lines = ''

    root = p.Node(i, None, None, None)

    p.recursive(root)

    #leaves are prime numbers in the prime factor tree
    leaves = []
    p.collectLeaves(leaves, root)

    lines += str(i).rjust(longest_num_len) + ': '
    for prime in sorted(leaves):
        lines += str(prime) + ', '
    lines = lines[:-2] + '\n'

    i+=1

open('primes.txt', 'a').write(lines[:-1])