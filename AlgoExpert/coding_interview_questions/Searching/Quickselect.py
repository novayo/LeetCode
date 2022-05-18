'''
main idea: quickselect
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''

import random

def quickselect(array, k):
    # Write your code here.
    
	def qs(l, r):
		if l > r:
			return 
		if l == r:
			return array[l]
		
		pivot_idx = random.randint(l, r)
		array[pivot_idx], array[r] = array[r], array[pivot_idx]
		
		i = l
		for j in range(l, r+1):
			if array[j] < array[r]:
				array[i], array[j] = array[j], array[i]
				i += 1
		array[i], array[r] = array[r], array[i]
		
		if i+1 == k:
			return array[i]
		elif i+1 > k:
			return qs(l, i-1)
		else:
			return qs(i+1, r)
	
	return qs(0, len(array)-1)
