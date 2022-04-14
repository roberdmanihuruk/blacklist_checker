# -*- coding: utf-8 -*-
"""blacklist_checker
Created by:
        Roberd (https://medium.com/@roberdmanihuruk17)

"""

def black_list_checker(sentence):
  black_list_word = ['hoax', 'bomb', 'terror']
  split_sentence = sentence.split(' ')
  check = False
  for x in black_list_word:
    for y in split_sentence:
      if x == y:
        check = True
        return print('Forbidden word found')
  return print('Forbidden word NOT found')

black_list_checker ('Delhi international airport received terror from a hoax bomb call on Monday')

black_list_checker ('Delhi international airport received a hoax call on Monday')

black_list_checker ('Delhi international airport received a call about bombing on Monday')




"""we can also check all few sentences at once by slightly modifying the code with tidyer results"""


def black_list_checker(sentence):
  black_list_word = ['hoax', 'bomb', 'terror']
  split_sentence = sentence.split(' ')
  check = False
  for x in black_list_word:
    for y in split_sentence:
      if x == y:
        check = True
        return print(sentence, '>>  Forbidden word found')
  return print(sentence,'>>  Forbidden word NOT found')

black_list_checker ('Delhi international airport received terror from a hoax bomb call on Monday')
black_list_checker ('Delhi international airport received a hoax call on Monday')
black_list_checker ('Delhi international airport received a call about bombing on Monday')
