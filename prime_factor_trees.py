'''
Andy Shaw
7/1/2014

Prime factor tree with graphic output to prime_output.txt
'''

import math
import sys

fill_char = '-'
tab_len = 4

class Node:
    def __init__(self, value, parent, lchild, rchild):
        self.value = value
        self.parent = parent   
        self.lchild = lchild
        self.rchild = rchild

def factor(n):
    #find a pair of factors somewhere in the middle
    #helps create a balanced tree
    mid = math.sqrt(n)
    i = int(math.floor(mid))
    while n%i != 0:
        i -= 1

    return i,n/i

def collectLeaves(leaves, root):
    if root.lchild == None and root.rchild == None:
        leaves.append(root.value)
        return
    else:
        if root.lchild: collectLeaves(leaves, root.lchild)
        if root.rchild: collectLeaves(leaves, root.rchild)

def printTree(root, depth=0, f=None):
    
    if root == None: return

    if not f: 
        print (fill_char*tab_len)*depth, root.value
    else:
        f.write((fill_char*tab_len)*depth + str(root.value) + '\n')
    
    printTree(root.lchild, depth+1, f)
    printTree(root.rchild, depth+1, f)

def recursive(root):
    n = root.value
    i,j = factor(n)

    if i == n or j == n: return

    root.lchild = Node(i, root, None, None)
    recursive(root.lchild)

    root.rchild = Node(j, root, None, None)
    recursive(root.rchild)

def count(l, e):
    n = 0
    for item in l:
        if item == e:
            n += 1
    return n

def main():
    n = int(sys.argv[1])

    leaves = []

    if n == 0: print 'Must be a non-zero integer'; exit()
    if n < 0: leaves.append(-1); n = n * -1

    root = Node(n, None, None, None)
    recursive(root)

    collectLeaves(leaves, root)

    f = open('prime_output.txt', 'w')
    printTree(root, 0, f)

    out = ''
    for prime in sorted(set(leaves)):
        out += str(prime) + '^' + str(count(leaves, prime)) + ', '
    f.write('\n' + out[:-2])

    f.close()

if __name__ == '__main__':
    main()