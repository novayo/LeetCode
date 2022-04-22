'''
main idea: dfs
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in input tree and d is the depth of input tree
'''
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
	ans = True
	
	def dfs(node):
		nonlocal ans
		
		if not ans:
			return 0
		
		if not node:
			return 0
		
		left = dfs(node.left)
		right = dfs(node.right)
		
		if abs(left - right) > 1:
			ans = False
		
		if not ans:
			return 0
		
		return max(left, right) + 1
	
	dfs(tree)
	return ans

