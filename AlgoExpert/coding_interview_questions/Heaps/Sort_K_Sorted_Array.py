'''
main idea: heap
time comp: O(nlogk)
space comp: O(k)
- where n is the length of the input array and k is the input integer
'''
import heapq

def sortKSortedArray(array, k):
    # Write your code here.
	hq = array[:k+1] # need to plus 1 because child1 & child2 is not ordered.
	heapq.heapify(hq)
	
	idx = k+1
	for i in range(len(array)):
		array[i] = heapq.heappop(hq)
		if idx < len(array):
			heapq.heappush(hq, array[idx])
			idx += 1
	
    return array

