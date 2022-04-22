'''
main idea: bfs
time comp: O(n)
space comp: O(w)
- where n is the number of nodes in input tree and w is the width of the input tree
'''

import collections

def invertBinaryTree(tree):
    # Write your code here.
    queue = collections.deque()
	queue.append(tree)
	
	while queue:
		node = queue.popleft()
		node.left, node.right = node.right, node.left
		
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	
	return tree

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

