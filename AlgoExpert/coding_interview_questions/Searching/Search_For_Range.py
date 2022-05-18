'''
main idea: bisect left & right
time comp: O(logn)
space comp: O(1)
- where n is the length of the input array
'''

def searchForRange(array, target):
    # Write your code here.
    def bisect_left(l, r):
		ans = -1
		while l <= r:
			mid = l + (r-l) // 2
			if array[mid] == target:
				ans = mid
				r = mid - 1
			elif array[mid] > target:
				r = mid - 1
			else:
				l = mid + 1
		return ans
	
	def bisect_right(l, r):
		ans = -1
		while l <= r:
			mid = l + (r-l) // 2
			if array[mid] == target:
				ans = mid
				l = mid + 1
			elif array[mid] > target:
				r = mid - 1
			else:
				l = mid + 1
		return ans
	
	return bisect_left(0, len(array)-1), bisect_right(0, len(array)-1)