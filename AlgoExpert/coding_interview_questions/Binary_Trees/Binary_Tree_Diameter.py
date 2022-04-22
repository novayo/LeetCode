'''
main idea: dfs
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in the input tree and d is the depth of the input tree
'''
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
	ans = 0
    def dfs(node):
		nonlocal ans
		
		if not node:
			return 0
		
		left = dfs(node.left)
		right = dfs(node.right)
		ans = max(ans, left + right)
		return max(left, right) + 1
	
	dfs(tree)
	return ans

