'''
main idea: stack
time comp: O(n)
space comp: O(w)
- where n is the number of nodes in the input tree and w is the maximum width of the input tree
'''
def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    stack = []
	while stack or tree:
		if tree:
			stack.append(tree)
			tree = tree.left
		else:
			tree = stack.pop()
			callback(tree)
			tree = tree.right
	