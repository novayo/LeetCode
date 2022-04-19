import bisect
'''
main idea: recursion
time comp: O(n^2)
space comp: O(n)
- where n is the length of the input array.
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
	# find next bigger and index
	n = len(preOrderTraversalValues)
	idx_preorder = 0
	def recr(l, r):
		nonlocal idx_preorder
		if l > r:
			return None
		
		node = BST(preOrderTraversalValues[idx_preorder])
		idx_preorder += 1
		
		if l == r:
			return node
		
		idx = n
		for i in range(idx_preorder, n):
			if preOrderTraversalValues[i] >= node.value:
				idx = i
				break
		
		node.left = recr(l+1, idx-1)
		node.right = recr(idx, r)
		return node
	
	return recr(0, len(preOrderTraversalValues)-1)
