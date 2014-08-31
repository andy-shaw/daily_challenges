'''
Andy Shaw
8/25/2014

Morse code audio

http://www.reddit.com/r/dailyprogrammer_ideas/comments/2dsua1/intermediatehard_convert_text_morse_code_audio/
International Morse code from http://en.wikipedia.org/wiki/Morse_code#mediaviewer/File:International_Morse_Code.svg
'''

from winsound import Beep
from time import sleep

FREQUENCY = 700
UNIT = .06

_UNIT = int(UNIT * 1000) #convert to milliseconds

PHRASE = 'CAN YOU UNDERSTAND THIS'

encoding = {
    'A' : '+-',
    'B' : '-+++',
    'C' : '-+-+',
    'D' : '-++',
    'E' : '+',
    'F' : '++-+',
    'G' : '--+',
    'H' : '++++',
    'I' : '++',
    'J' : '+---',
    'K' : '-+-',
    'L' : '+-++',
    'M' : '--',
    'N' : '-+',
    'O' : '---',
    'P' : '+--+',
    'Q' : '--+-',
    'R' : '+-+',
    'S' : '+++',
    'T' : '-',
    'U' : '++-',
    'V' : '+++-',
    'W' : '+--',
    'X' : '-++-',
    'Y' : '-+--',
    'Z' : '--++',
    '0' : '-----',
    '1' : '+----',
    '2' : '++---',
    '3' : '+++--',
    '4' : '++++-',
    '5' : '+++++',
    '6' : '-++++',
    '7' : '--+++',
    '8' : '---++',
    '9' : '----+'
}

def morse(letter):
    code = encoding[letter]
    for b in code:
        if b == '-':
            Beep(FREQUENCY, _UNIT * 3)
        elif b == '+':
            Beep(FREQUENCY, _UNIT * 1)
        sleep(UNIT)

if __name__ == '__main__':
    for word in PHRASE.split():
        for letter in word:
            morse(letter)
        sleep(UNIT*3)
    sleep(UNIT*7)