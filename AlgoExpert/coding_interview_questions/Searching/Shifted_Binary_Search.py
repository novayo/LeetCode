'''
main idea: find peak
time comp: O(logn)
space comp: O(1)
- where n is the length of the input array
'''
def shiftedBinarySearch(array, target):
    # Write your code here.
	def bisect_left(l, r):
		while l <= r:
			mid = l + (r-l) // 2
			if array[mid] == target:
				return mid
			elif array[mid] > target:
				r = mid - 1
			else:
				l = mid + 1
		return -1
	
	l, r = 0, len(array)-1
	
	while l <= r:
		mid = l + (r-l) // 2
		if array[0] > array[mid]:
			r = mid - 1
		elif mid+1 >= len(array):
			l = mid
			break
		elif array[mid] > array[mid+1]:
			l = mid
			break
		else:
			l = mid+1
	
	if array[0] <= target <= array[l]:
		return bisect_left(0, l)
	else:
		return bisect_left(l+1, len(array)-1)
	
	
