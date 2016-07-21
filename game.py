'''
Make a number guesser!
'''
import random
import sys
from time import sleep

answer = int(random.random() * 100)
print 'I have a secret number! Can you guess it?'


def guess(number):
    print 'You guessed {0}, let me think...'.format(number)
    sleep(1)
    if number == answer:
        print '>> Correct :)'
        sys.exit(0)
    elif number < answer:
        print '>> too low :( guess again'
        return 'too low'
    elif number > answer:
        print '>> too high :( guess again'
        return 'too high'
