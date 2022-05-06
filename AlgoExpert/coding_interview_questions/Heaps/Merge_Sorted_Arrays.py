'''
main idea: heap
time comp: O(nlogh)
space comp: O(n)
- where n is the total number of array elements and h is the number of arrays
'''
import heapq

def mergeSortedArrays(arrays):
    # Write your code here.
	hq = []
    for i in range(len(arrays)):
		heapq.heappush(hq, (arrays[i][0], i, 0))
	
	ans = []
	while hq:
		v, i, j = heapq.heappop(hq)
		ans.append(v)
		
		if j == len(arrays[i])-1:
			continue
		heapq.heappush(hq, (arrays[i][j+1], i, j+1))
	return ans
