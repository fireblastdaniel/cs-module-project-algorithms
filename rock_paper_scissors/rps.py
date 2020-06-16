#!/usr/bin/python

import sys
import math

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  
  output = [[] for _ in range(3**n)]
  rps_recursion(0, n, output)
  return output

def rps_recursion(n, max_n, arr):
  one_third = len(arr) // 3
  two_thirds = 2 * one_third

  for i in range(0, one_third):
    arr[i].append('rock')

  for i in range(one_third, two_thirds):
    arr[i].append('paper')

  for i in range(two_thirds, len(arr)):
    arr[i].append('scissors')

  if n < max_n - 1:
    rps_recursion(n+1, max_n, arr[:one_third])
    rps_recursion(n+1, max_n, arr[one_third:two_thirds])
    rps_recursion(n+1, max_n, arr[two_thirds:])


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')