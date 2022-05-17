'''
main idea: heap
time comp: O(nlog3)
space comp: O(3)
- where n is the length of input array
'''

import heapq

def findThreeLargestNumbers(array):
    # Write your code here.
    min_heap = []
	
	for a in array:
		heapq.heappush(min_heap, a)
		
		if len(min_heap) > 3:
			heapq.heappop(min_heap)
	
	ans = []
	while min_heap:
		ans.append(heapq.heappop(min_heap))
	return ans
