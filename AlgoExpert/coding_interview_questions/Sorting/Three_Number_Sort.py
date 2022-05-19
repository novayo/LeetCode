'''
main idea: swap
time comp: O(nm)
space comp: O(1)
- where n is the length of the input array and m is the length of the input order
'''
def threeNumberSort(array, order):
    # Write your code here.
	idx = 0
    for target in order:
		for i in range(idx, len(array)):
			if array[i] == target:
				array[i], array[idx] = array[idx], array[i]
				idx += 1
	return array

