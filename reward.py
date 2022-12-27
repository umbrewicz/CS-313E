#  File: reward.py

#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.
#  Student Name: Nick Umbrewicz
#  Student UT EID: nju95
#  Course Name: CS 313E
#  Unique Number: 52520

import sys

max_val = 1000


def getmin(prices, T):
	reward_amount = int(0.1 * T)
	dp_table = [[0 for i in range(reward_amount + 1)] for i in range(len(prices) + 1)]

	for i in range(1, reward_amount + 1):
		dp_table[0][i] = max_val

	for i in range(1, len(prices) + 1):
		for j in range(1, reward_amount + 1):
			if prices[i-1] > j:
				dp_table[i][j] = dp_table[i - 1][j]
			else:
				dp_table[i][j] = min(dp_table[i-1][j], dp_table[i][j - prices[i-1]] + 1)
	
	if dp_table[i][j] == max_val:
		return -1

	return dp_table[len(prices)][reward_amount]



if __name__ == "__main__":

	# Read input list of prices for each gift
	prices_str = sys.stdin.readline().split()
	prices = [ int(x) for x in prices_str ]

	# Read total price that the customer spends
	T = int(sys.stdin.readline())

	print(getmin(prices, T))
