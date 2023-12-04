#!/usr/bin/python3

import sys
import re
import functools

def main():
  input = read_file(sys.argv[1])
  print("Input", input)
  
  score = 0
  
  for card in input:
    score = score + get_card_score(card)
    
  print("Score", score)
  
def get_card_score(card):
  split_card = card.split("|")
  winning_numbers = list(re.findall(r'\d+', split_card[0].split(":")[1]))
  winning_numbers.sort()
  actual_numbers = list(re.findall(r'\d+', split_card[1]))
  actual_numbers.sort()
  print("Winning", winning_numbers)
  print("Actual", actual_numbers)
  
  winning_count = 0
  for number in actual_numbers:
    try:
      index = winning_numbers.index(number)
      if winning_count == 0:
        winning_count = winning_count + 1
      else:
        winning_count = winning_count * 2
    except ValueError:
      continue
  print("Card score", winning_count)
  return winning_count
  
def read_file(filename):
  file = open(filename, 'r')
  file_contents = file.readlines()
  file.close()
  return file_contents

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()