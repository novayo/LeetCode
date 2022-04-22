'''
main idea: morris traversal
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in the input tree
'''
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
	find = False
    while tree:
		if not tree.left:
			if find:
				return tree
			elif tree == node:
				find = True
			tree = tree.right
		else:
			p = tree.left
			while p.right and p.right != tree:
				p = p.right
			
			if p.right != tree:
				p.right = tree
				tree = tree.left
			else:
				p.right = None
				if find:
					return tree
				elif tree == node:
					find = True
				tree = tree.right
			
	return None

