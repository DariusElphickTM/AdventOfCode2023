#!/usr/bin/python3

import sys
import re

def main():
  input = read_file(sys.argv[1])
  print("Input", input)
  
  calibrationValues = []
  for line in input:
    calibrationValues.append(process_line(line))
  print(calibrationValues)
  
  answer = 0
  for line in calibrationValues:
    answer = answer + int(line)
  print(answer)
  
def process_line(line):
  numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
  number_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }
  for i in range(len(numbers)):
    number = numbers[i]
    if(number in number_map):
      numbers[i] = number_map[number]
  return "%s%s" % (numbers[0], numbers[-1])
  
def read_file(filename):
  file = open(filename, 'r')
  file_contents = file.readlines()
  file.close()
  return file_contents

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()