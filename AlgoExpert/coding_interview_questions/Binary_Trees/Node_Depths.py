'''
main idea: recursion
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in input tree and d is the depth of the input tree
'''
def nodeDepths(root):
    # Write your code here.
    def dfs(node, layer=0):
		if not node:
			return 0
		
		return layer + dfs(node.left, layer+1) + dfs(node.right, layer+1)
	
	return dfs(root)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

