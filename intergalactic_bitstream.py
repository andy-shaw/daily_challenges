'''
Andy Shaw
8/3/2014

Create a compression algorithm to shrink a 140 byte string.

Prompt: http://www.reddit.com/r/dailyprogrammer/comments/2b21mp/7182014_challenge_171_hard_intergalatic_bitstream/

'''

import math
import string

infile = 'bitstream_input.txt'
encoding = {}
deliminator = '00'

#pre-calculated frequency of letters based on a separate dictionary with digits at the end
sorted_letters =   [' ', 'E', 'S', 'I', 'A', 'R', 'N', 
                    'T', 'O', 'L', 'C', 'D', 'U', 'P',
                    'M', 'G', 'H', 'B', 'Y', 'F', 'V',
                    'K', 'W', 'Z', 'X', 'Q', 'J', '0',
                    '1', '2', '3', '4', '5', '6', '7',
                    '8', '9']

def create_encoding():
    #encoding is the same every time, I was simply lazy in writing out the binary by hand
    i = 1
    for c in sorted_letters:
        t = str(bin(i))[2:]

        #remove 001 from being in any of the encodings
        while deliminator + '1' in t:
            i += 1
            t = str(bin(i))[2:]
        encoding[c] = t
        i += 1

def compress(text):
    '''compress text'''
    result = ''
    for letter in text:
        result += deliminator + encoding[letter]

    return result, len(result)

def decompress(text):
    '''decompress provided text'''
    result = ''
    words = get_words(text)
    for word in words:
        for key, val in encoding.items():
            #remove deliminator
            if val == word[2:]:
                result += key

    return result

def get_words(text):
    current = 0
    next = 3
    words = []

    while next < len(text):
        #end of message checked first
        if text[next:next+3] == '001':
            #char has been found
            words.append(text[current:next])
            current = next
        next += 1
    #add last word
    words.append(text[current:])

    return words

def main(in_text):

    #print stats
    print 'Message:', in_text
    print 'Read message of {0} bytes.'.format(len(in_text))

    #populate encoding table
    create_encoding()

    compressed, bit_count = compress(in_text)

    print 'Compressing {0} bits into {1} bits. ({2}% compression)'.format(len(in_text)*8, bit_count, 100*(1 - bit_count/float(len(in_text)*8)))
    print 'Sending message.'

    result = decompress(compressed)

    print 'Decompressing message into {0} bytes.'.format(len(result))

    if in_text == result:
        print 'Message matches!'
    else:
        print 'Error in transmission.  Resend.'

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) > 1:
        if args[1].upper() == 'DEBUG':
            debug = True

  
    #parse input
    for line in open(infile, 'r').readlines():
        if '|' != line[0]:
            main(line.strip())
            print ''