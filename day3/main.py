#!/usr/bin/python3

import sys
import re
import functools

def main():
  input = read_file(sys.argv[1])
  print("Input", input)
  
  symbol_locations = get_symbol_locations(input)
  #print_location_map(symbol_locations, "Symbol Locations")
      
  number_locations = get_number_locations(input)
  #print_location_map(number_locations, "Number Locations")
  
  parts = get_parts(symbol_locations, number_locations)
  print("Parts", parts)
  
  counter = 0
  for part in parts:
    counter = counter + int(part)
  print("Answer", counter)
  
def get_parts(symbol_locations, number_locations):
  parts = []
  for i, line in enumerate(symbol_locations):
    for symbol in line:
      
      matches = []
      
      if i > 0:
        print("Above line", symbol)
        numbers_above = number_locations[i - 1]
        for number in numbers_above:
          print("Comparing symbol", symbol)
          print("Comparing number", number)
          if (symbol.start() == number.end()) or (symbol.end() == number.start()) or (symbol.start() >= number.start() and symbol.start() <= number.end()):
            print("MATCH ABOVE!")
            matches.append(number[0])
            
      print("Same line", symbol)
      numbers_on_same_line = number_locations[i]
      for number in numbers_on_same_line:
        print("Comparing symbol", symbol)
        print("Comparing number", number)
        if (symbol.start() == number.end()) or (symbol.end() == number.start()):
          print("MATCH ON LINE!")
          matches.append(number[0])
          
      if i < len(symbol_locations) - 1:
        print("Below line", symbol)
        numbers_below = number_locations[i + 1]
        for number in numbers_below:
          print("Comparing symbol", symbol)
          print("Comparing number", number)
          if (symbol.start() == number.end()) or (symbol.end() == number.start()) or (symbol.start() >= number.start() and symbol.start() <= number.end()):
            print("MATCH BELOW!")
            matches.append(number[0])
            
      if len(matches) == 2 and symbol[0] == '*':
        parts.append(functools.reduce(lambda a, b: int(a) * int(b), matches))
        
  return parts
  
def get_symbol_locations(input):
  symbol_locations = []
  for line in input:
    symbol_locations.append(list(re.finditer(r'[^\d\n.]', line)))
  return symbol_locations

def get_number_locations(input):
  number_locations = []
  for line in input:
    number_locations.append(list(re.finditer(r'\d+', line)))
  return number_locations

def print_location_map(location_map, label):
  print(label)
  for line_matches in location_map:
    for match in line_matches:
      print(match)
  
def read_file(filename):
  file = open(filename, 'r')
  file_contents = file.readlines()
  file.close()
  return file_contents

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()