#  File: toomany.py

#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.

#  Student Name: Nick Umbrewicz

#  Student UT EID: nju96

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list, N):
	# make a dictionary based on flower_list to find the
	# types of flowers and number of each type of flower
	my_dict = {}
	for flower in flower_list:
		if flower in my_dict:
			my_dict[flower] += 1
		else:
			my_dict[flower] = 1

	# if the value of my_dict[key] > N * 2 (i.e., more than 2
	# flowers per vase), append the key (i.e., flower type) to
	# bought_too_many and eventually return sorted list
	bought_too_many = []

	for key in my_dict:
		if my_dict[key] > N * 2:
			bought_too_many.append(key)
			
	return sorted(bought_too_many)


if __name__ == '__main__':

	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [ int(x) for x in flower_list_str ]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)
