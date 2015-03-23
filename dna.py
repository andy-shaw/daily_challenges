'''
Andy Shaw
3/23/2015

This program will implement the challenges for the DNA daily programmer challenges.

http://www.reddit.com/r/dailyprogrammer/comments/2zyipu/20150323_challenge_207_easy_bioinformatics_1_dna/
'''


def get_pair(base):
    pairs = {
        'T' : 'A',
        'A' : 'T',
        'G' : 'C',
        'C' : 'G'
    }
    return pairs[base]

def get_codon(a,b,c):
    codons = {
        'GCT' : 'Ala',
        'GCC' : 'Ala',
        'GCA' : 'Ala',
        'GCG' : 'Ala',

        'CGT' : 'Arg',
        'CGC' : 'Arg',
        'CGA' : 'Arg',
        'CGG' : 'Arg',
        'AGA' : 'Arg',
        'AGG' : 'Arg',

        'AAT' : 'Asn',
        'AAC' : 'Asn',

        'GAT' : 'Asp',
        'GAC' : 'Asp',

        'TGT' : 'Cys',
        'TGC' : 'Cys',

        'CAA' : 'Gln',
        'CAG' : 'Gln',

        'GAA' : 'Glu',
        'GAG' : 'Glu',

        'GGT' : 'Gly',
        'GGC' : 'Gly',
        'GGA' : 'Gly',
        'GGG' : 'Gly',

        'CAT' : 'His',
        'CAC' : 'His',

        'ATT' : 'Ile',
        'ATC' : 'Ile',
        'ATA' : 'Ile',

        'ATG' : 'START',

        'TTA' : 'Leu',
        'TTG' : 'Leu',
        'CTT' : 'Leu',
        'CTC' : 'Leu',
        'CTA' : 'Leu',
        'CTG' : 'Leu',

        'AAA' : 'Lys',
        'AAG' : 'Lys',

        'ATG' : 'Met',

        'TTT' : 'Phe',
        'TTC' : 'Phe',

        'CCT' : 'Pro',
        'CCC' : 'Pro',
        'CCA' : 'Pro',
        'CCG' : 'Pro',

        'TCT' : 'Ser',
        'TCC' : 'Ser',
        'TCA' : 'Ser',
        'TCG' : 'Ser',
        'AGT' : 'Ser',
        'AGC' : 'Ser',

        'ACT' : 'Thr',
        'ACC' : 'Thr',
        'ACA' : 'Thr',
        'ACG' : 'Thr',

        'TGG' : 'Trp',

        'TAT' : 'Tyr',
        'TAC' : 'Tyr',

        'GTT' : 'Val',
        'GTC' : 'Val',
        'GTA' : 'Val',
        'GTG' : 'Val',

        'TAA' : 'STOP',
        'TGA' : 'STOP',
        'TAG' : 'STOP'
    }
    return codons[a+b+c]

def is_start(a,b,c):
    return a+b+c == 'ATG'

def is_stop(a,b,c):
    return a+b+c in ['TAA', 'TGA', 'TAG']

def find_start_codon(sequence):
    '''return the index of the first char of the start codon triplet'''
    for i in range(len(sequence)):
        if i+3 >= len(sequence): return -1

        if is_start(sequence[i], sequence[i+1], sequence[i+2]): return i

if __name__ == '__main__':
    import sys

    s = ''.join(sys.argv[1:])

    for base in s:
        print base + ' ',

    print ''

    for i in range(0,len(s), 3):
        if i+3 >= len(s): print get_codon(*s[i:]); break
        if i == 0: print 'START',

        print get_codon(*s[i:i+3]) + ' ',