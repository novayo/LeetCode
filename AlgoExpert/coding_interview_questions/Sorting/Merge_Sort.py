'''
main idea: merge sort
time comp: O(nlogn)
space comp: O(logn)
'''
def mergeSort(array):
    # Write your code here.
    
	def mergesort(l, r):
		if l > r:
			return []
		if l == r:
			return [array[l]]
		
		mid = l + (r-l) // 2
		left = mergesort(l, mid)
		right = mergesort(mid+1, r)
		
		merged = []
		i = j = 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				merged.append(left[i])
				i += 1
			else:
				merged.append(right[j])
				j += 1
		
		if i < len(left):
			merged.extend(left[i:])
		if j < len(right):
			merged.extend(right[j:])
		
		return merged
	
	return mergesort(0, len(array)-1)
