'''
main idea: find target node and bfs from it to find specific layer
time comp: O(n)
space comp: O(n)
- where n is the number of the input tree
'''

import collections

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
	ans = []
	
	# find the target node
	target_node = None
	queue = collections.deque()
	
	queue.append(tree)
	while queue:
		node = queue.popleft()
		
		if node.value == target:
			target_node = node
			break
		
		if node.left:
			node.left.parent = node
			queue.append(node.left)
		if node.right:
			node.right.parent = node
			queue.append(node.right)
	
	if not target_node:
		return ans
	
	# do bfs from target node
	visited = set()
	queue = collections.deque()
	
	visited.add(target_node.value)
	queue.append((target_node, 0)) # node, layer
	while queue:
		node, layer = queue.popleft()
		
		if layer == k:
			ans.append(node.value)
			continue
		
		if hasattr(node, 'parent') and node.parent.value not in visited:
			visited.add(node.parent.value)
			queue.append((node.parent, layer+1))
		
		if node.left and node.left.value not in visited:
			visited.add(node.left.value)
			queue.append((node.left, layer+1))
		
		if node.right and node.right.value not in visited:
			visited.add(node.right.value)
			queue.append((node.right, layer+1))
		
    return ans

