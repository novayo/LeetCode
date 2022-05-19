'''
main idea: insertion sort
time comp: O(n^2)
space comp: O(1)
'''
def insertionSort(array):
    # Write your code here.
    for i in range(len(array)):
		print(i, array[i])
		for j in range(i, 0, -1):
			if array[j-1] > array[j]:
				array[j], array[j-1] = array[j-1], array[j]
	return array

