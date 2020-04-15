#!/usr/bin/python

import argparse

def find_max_profit(prices):
#find highest_value in list
    highest_value = max(prices[1:])
    # print(highest_value)

#find lowest_value in list that occurs before the highest value
    for i in prices:
        temp_arr = prices.index(highest_value)
    # print(temp_arr)
    lowest_value = min(prices[:temp_arr])
    # print(lowest_value)

#max_profit = highest_value - lowest_value
    profit = highest_value - lowest_value
    # print(profit)
    return profit
# find_max_profit(prices)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))