'''
main idea: quicksort
time comp: O(nlogn)
space comp: O(logn)
- where n is the length of the input array
'''

import random

def quickSort(array):
    # Write your code here.
	if not array:
		return array

	pivot = array[random.randint(0, len(array)-1)]

	less = []
	equals = 0
	greater = []

	for val in array:
		if val < pivot:
			less.append(val)
		elif val == pivot:
			equals += 1
		else:
			greater.append(val)

	return quickSort(less) + [pivot] * equals + quickSort(greater)	
