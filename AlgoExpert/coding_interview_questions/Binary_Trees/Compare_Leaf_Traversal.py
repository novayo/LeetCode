'''
main idea: dfs
time comp: O(n+m)
space comp: O(max(h1, h2))
- where n is the number of nodes in the first Binary Tree, m is the number in the second, h1 is the height of the first Binary Tree, and h2 is the height of the second.
'''
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal(tree1, tree2):
    # Write your code here.
    return getLeaves(tree1) == getLeaves(tree2)

def getLeaves(root):
	ret = []
	def dfs(node):
		nonlocal ret
		
		if not node:
			return
		if not node.left and not node.right:
			ret.append(node.value)
			return
		
		dfs(node.left)
		dfs(node.right)
	dfs(root)
	return ret