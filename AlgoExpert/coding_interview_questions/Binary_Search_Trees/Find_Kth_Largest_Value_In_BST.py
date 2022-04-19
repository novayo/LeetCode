'''
main idea: reversed inorder
time comp: O(h+k)
space comp: O(h)
- where h is the height of the input tree and k is the input parameter.
'''

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
	stack = []
	_k = 0
	while stack or tree:
		if tree:
			stack.append(tree)
			tree = tree.right
		else:
			tree = stack.pop()
			_k += 1
			if _k == k:
				return tree.value
			tree = tree.left
    return -1
