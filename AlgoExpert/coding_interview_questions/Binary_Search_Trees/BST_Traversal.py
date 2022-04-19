'''
main idea: recursion / iterative / morris
time comp: O(n) / O(n) / O(n)
space comp: O(d) / O(d) / O(1)
- where n is the number of the tree and d is the depth of the tree.
'''

def inOrderTraverse(tree, array):
    # Write your code here.
	while tree:
		if not tree.left:
			array.append(tree.value)
			tree = tree.right
		else:
			p = tree.left
			while p.right and p.right != tree:
				p = p.right
			
			if not p.right:
				p.right = tree
				tree = tree.left
			else:
				p.right = None
				array.append(tree.value)
				tree = tree.right
	return array

def preOrderTraverse(tree, array):
    # Write your code here.
    stack = []
	while stack or tree:
		if tree:
			stack.append(tree)
			array.append(tree.value)
			tree = tree.left
		else:
			tree = stack.pop()
			tree = tree.right
	return array

def postOrderTraverse(tree, array):
    # Write your code here.
    def recr(node):
		if not node:
			return
		recr(node.left)
		recr(node.right)
		array.append(node.value)
	recr(tree)
	return array
