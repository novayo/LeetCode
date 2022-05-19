'''
main idea: selection sort
time comp: O(n^2)
space comp: O(1)
- where n is the length of the input array
'''
def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
		cur, idx = float('inf'), -1
		for j in range(i, len(array)):
			if array[j] < cur:
				cur = array[j]
				idx = j
		array[i], array[idx] = array[idx], array[i]
		
	return array
