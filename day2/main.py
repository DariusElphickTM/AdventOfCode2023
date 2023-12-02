#!/usr/bin/python3

import sys
import re

def main():
  actual_red = int(sys.argv[2])
  actual_green = int(sys.argv[3])
  actual_blue = int(sys.argv[4])
  input = read_file(sys.argv[1])
  print("Input", input)
  games = list(map(interpret_game, input))
  print("Games", games)
  count = 0
  for game in games:
    count = count + (game['blue'] * game['green'] * game['red'])
    """if(actual_blue >= game['blue'] and actual_green >= game['green'] and actual_red >= game['red']):
      print("Possible", game['id'])
      count = count + int(game['id'])"""
  print("Count", count)

def interpret_game(line):
  game = re.split(r'\:', line)
  game[0] = re.sub('Game ', '', game[0])
  reds = list(map(int, re.findall(r'\d+(?= red)', game[1])))
  blues = list(map(int, re.findall(r'\d+(?= blue)', game[1])))
  greens = list(map(int, re.findall(r'\d+(?= green)', game[1])))
  return {
    'id': game[0],
    'red': max(reds),
    'green': max(greens),
    'blue': max(blues)
  }
  
def read_file(filename):
  file = open(filename, 'r')
  file_contents = file.readlines()
  file.close()
  return file_contents

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()