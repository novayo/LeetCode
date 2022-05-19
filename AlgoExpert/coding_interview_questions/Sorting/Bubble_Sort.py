'''
main idea: bubble sort
time comp: O(n^2)
space comp: O(1)
- where n is the length of the input array
'''
def bubbleSort(array):
    # Write your code here.
	
    for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	
	return array

