'''
main idea: recursion
time comp: O(n)
space comp: O(n)
- where n is the length of input array.
'''
def minHeightBst(array):
    def build(i, j):
		if i > j:
			return None
		if i == j:
			return BST(array[i])
		
		mid = i + (j-i) // 2
		left = build(i, mid-1)
		right = build(mid+1, j)
		return BST(array[mid], left, right)
	
	return build(0, len(array)-1)

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

