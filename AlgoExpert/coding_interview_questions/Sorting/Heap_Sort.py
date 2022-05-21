'''
main idea: heap sort
time comp: O(logn)
space comp: O(1)
'''

def heapSort(array):
    # Write your code here.
	array = [-val for val in array]
	heapify(array)
	for i in range(len(array)-1, -1, -1):
		array[0], array[i] = array[i], array[0]
		shiftDown(0, i-1, array)
	return [-val for val in array]

def heapify(array):
	idx = (len(array)-1) // 2
	for i in range(idx, -1, -1):
		shiftDown(i, len(array)-1, array)

def shiftDown(i, j, array):
	child1 = i * 2 + 1
	while child1 <= j:
		child2 = i * 2 + 2
		if child2 <= j and array[child2] < array[child1]:
			idx = child2
		else:
			idx = child1
		
		if array[i] > array[idx]:
			array[i], array[idx] = array[idx], array[i]
			i = idx
			child1 = i * 2 + 1
		else:
			break
		
