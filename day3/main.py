#!/usr/bin/python3

import sys
import re

def main():
  input = read_file(sys.argv[1])
  print("Input", input)
  
def read_file(filename):
  file = open(filename, 'r')
  file_contents = file.readlines()
  file.close()
  return file_contents

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()