'''
main idea: morris, successor => right / predecessor => left
time comp: O(n)
space comp: O(1)
- where n is the number of the input tree
'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
	node = root
	pre = None
    while root:
		if not root.left:
			root.left = pre
			if pre:
				pre.right = root
			pre = root
			root = root.right
		else:
			p = root.left
			while p.right and p.right != root:
				p = p.right
			
			if p.right != root:
				p.right = root
				root = root.left
			else:
				p.right = None
				root.left = pre
				if pre:
					pre.right = root
				pre = root
				root = root.right
	
	while node and node.left:
		node = node.left
		
	return node
