'''
Andy Shaw
7/5/2014

http://www.reddit.com/r/dailyprogrammer/comments/263dp1/5212014_challenge_163_intermediate_fallouts/
'''

import dictionary
import random

#difficulty: (length of word, word count)
LEVELS = {1:(5, 4), 2:(7, 7), 3:(9, 9), 4:(12, 12), 5:(15, 15)}

def main(length, word_count):
    #get random set of words from dictionary
    words = dictionary.fetch(length)
    words = random.sample(words, word_count)

    answer = words[random.randint(0,word_count-1)]
    tries = 4

    #print choices
    for word in words:
        print word.upper()

    while tries > 0:
        guess = raw_input('Guess (' + str(tries) + ' left)? ')

        #error checking of input
        failed = False
        digit = False
        if len(guess) != length:
            print 'Invalid guess: guess needs to be', length, 'characters long'
            failed = True
        
        for c in guess:
            if c.isdigit():
                digit = True
        if digit:
            print 'Invalid guess: guess cannot contain numbers'
            failed = True

        if guess not in words:
            print 'Invalid guess: word not valid from list'
            failed = True

        if failed: continue

        #check guess against answer
        matches = 0
        for i in range(len(guess)):
            if guess[i].upper() == answer[i].upper():
                matches += 1

        if matches == length:
            print 'Success.  Terminal is now unlocked.'
            return

        print "{0}/{1} correct".format(matches, length)


        tries -= 1

        if tries == 0:
            print 'You have failed. Terminal is now locked.'


if __name__ == '__main__':
    difficulty = raw_input('Difficulty (1-5)?\n')
    try:
        d = int(difficulty)
        if not 1 <= d <= 5: raise ValueError
    except ValueError:
        print 'Invalid difficulty: enter a number between 1 and 5'
        exit()

    main(LEVELS[int(difficulty)][0],LEVELS[int(difficulty)][1])