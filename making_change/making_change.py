#!/usr/bin/python

import sys

def making_change(amount, denominations, memo = {}):

  if amount in memo:
    if len(denominations) in memo[amount]:
      return memo[amount][len(denominations)]

  output = 0
  max_amount = denominations[-1]
  max_coins = int(amount / max_amount)

  if len(denominations) == 1:
    return 1

  if max_coins == 0:
    return making_change(amount, denominations[:-1])

  for i in range(0, max_coins + 1):
    sub_total = amount - i * max_amount
    output += making_change(sub_total, denominations[:-1])

  if amount not in memo:
    memo[amount] = {}

  memo[amount][len(denominations)] = output
  return output


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")