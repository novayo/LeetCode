'''
main idea: dfs
time comp: O(logn)
space comp: O(d)
- where n is the number of nodes in BST and d is the depth of BST
'''
def findClosestValueInBst(tree, target):
    # Write your code here.
	def dfs(node):
		if not node:
			return float('inf'), 0 # diff, ans
		
		
		diff = abs(node.value - target) 
		if node.value < target:
			right = dfs(node.right)
			if (diff < right[0]):
				return diff, node.value
			else:
				return right
		elif node.value > target:
			left = dfs(node.left)
			if (diff < left[0]):
				return diff, node.value
			else:
				return left
		else:
			return 0, node.value
	
	return dfs(tree)[1]
		
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
