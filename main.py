#class

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
  incorrect_list_prompt = input('\nWould you like to add \'{}\' to your review list? (yes/no)\n'.format(arabic_text(tple[0])))
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
    attempt = input('\nWhat is {} in English?\n'.format(arabic))

    answer = '\n --------------------\nThe answer is \'{}\'\n --------------------'.format(english)
    print(answer)

  return

def random_test(lst, total_questions): 
  incorrect_list = []
  question_number = 1
  while question_number <= total_questions: 
    index_position = random.choice((range(len(lst))))
    tple = lst[index_position]
    word_attempt(tple, incorrect_list)
    question_number += 1
  if len(incorrect_list) > 0:
    words = pd.DataFrame(incorrect_list, columns = ['Arabic', 'English'])
    print('\nThe word(s) that you selected were: \n')  
    print(words)
  
    retest = input('\nWould you like to review the words you selected? (yes/no)\n')
    yes_command = (retest == 'yes' or retest == 'Yes' or retest == 'yes ' or retest == 'Yes ')
    if yes_command:
      print(' --------------------\n')
      complete_test(incorrect_list)
      print('\nHere is your review list again:\n')
      print(words)
  return

def setup():
  print('Which of the following lists would you like to be tested on?\n')
  print(' - chapter 1 roots vocab list (1a)\n')
  vocab_list = input('Please type the list key (eg. 1a).\n')
  question_number_input = input('How many questions would you like?\n')
  total_questions = int(question_number_input)
  if str(vocab_list) == '1a' or str(vocab_list) == '1a ':
    random_test(chapter1_roots_vocab_list, total_questions)
  return


setup()