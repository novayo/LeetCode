'''
main idea: morris
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in the input tree
'''
def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    while tree:
		if not tree.left:
			callback(tree)
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
				callback(tree)
				tree = tree.right