#class, dataframe, error with arabic for retest

import random
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display

chapter1_roots_vocab_list = [('ظول', 'length, height'), ('صاحب', 'friend; owner'), ('اثتهر ب', 'to be famous for'), ('حقيق', 'truth, fact'), ('حفظ', 'to memorise; keep, preserve'), ('بلدة ', 'town'), ('عالم ج علماء', 'learned person, scientist'), ('معلومات', 'information')]

def arabic_text(text):
  reshaped_text = arabic_reshaper.reshape(text)    
  bidi_text = get_display(reshaped_text) 
  return bidi_text

def incorrect_function(tple, incorrect_list):
  incorrect_list_prompt = input('\nWould you like to add \'{}\' to your incorrect list? (yes/no)\n'.format(arabic_text(tple[0])))
  yes_command = (incorrect_list_prompt == 'yes' or incorrect_list_prompt == 'Yes' or incorrect_list_prompt == 'yes ' or incorrect_list_prompt == 'Yes ')
  if yes_command:
    arabic = arabic_text(tple[0])
    english = (tple[1])
    added_word = (arabic, english)
    return incorrect_list.append(added_word)
    
def word_attempt(tple, incorrect_list):

  attempt = input('\nWhat is {} in English?\n'.format(arabic_text(tple[0])))

  answer = '\n --------------------\nThe answer is \'{}\'\n --------------------'.format(tple[1])
  print(answer)

  incorrect_function(tple, incorrect_list)

  return
  
def complete_test(lst):
  for i in range(len(lst)):
    arabic, english = lst[i]
    arabic_fixed = arabic_text(arabic)
    attempt = input('\nWhat is {} in English?\n'.format(arabic_fixed))

    answer = '\n --------------------\nThe answer is \'{}\'\n --------------------'.format(english)
    print(answer)

  return

def random_test(lst): 
  incorrect_list = []
  question_number_input = input('How many questions would you like?\n')
  total_questions = int(question_number_input)
  question_number = 1
  while question_number <= total_questions: 
    index_position = random.choice((range(len(lst))))
    tple = lst[index_position]
    word_attempt(tple, incorrect_list)
    question_number += 1
  print('\nThe word(s) that you got incorrect were: \n {}'.format(incorrect_list))
  
  retest = input('\nWould you like a test on the words which you got wrong? (yes/no)\n')
  yes_command = (retest == 'yes' or retest == 'Yes' or retest == 'yes ' or retest == 'Yes ')
  if yes_command:
    print(' --------------------\n')
    complete_test(incorrect_list)
  return


random_test(chapter1_roots_vocab_list)
