'''
main idea: dfs
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in input tree and d is the depth of input tree
'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    # Write your code here.
    def dfs(node, parent, isLeft):
		if not node:
			return
		left, right = node.left, node.right
		
		dfs(left, node, True)
		# for root
		if not parent:
			node.right = None
		elif isLeft:
			node.right = parent.right
		elif parent.right:
			node.right = parent.right.left
		else:
			node.right = None
		
		dfs(right, node, False)
	dfs(root, None, True)
	return root