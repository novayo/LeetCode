'''
main idea: binary search
time comp: O(logn)
space comp: O(1)
- where n is the length of input array
'''
def indexEqualsValue(array):
    # Write your code here.
    l, r = 0, len(array)-1
	ans = -1
	
	while l <= r:
		mid = l + (r-l) // 2
		if array[mid] == mid:
			ans = mid
			r = mid - 1
		elif array[mid] > mid:
			r = mid - 1
		else:
			l = mid + 1
	return ans
