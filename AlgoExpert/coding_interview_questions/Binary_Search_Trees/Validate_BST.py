'''
main idea: dfs
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in the BST and d is the depth of the BST
'''

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
	ans = True
	
	def dfs(node):
		nonlocal ans
		if not ans:
			return 0, 0
		
		if not node:
			return float('inf'), -float('inf')
		if not node.left and not node.right:
			return node.value, node.value
	
		l_min, l_max = dfs(node.left)
		r_min, r_max = dfs(node.right)
		
		if not (l_max < node.value <= r_min):
			ans = False
			return 0, 0
		
		return min(l_min, r_min), max(l_max, r_max)
	
	dfs(tree)
	return ans