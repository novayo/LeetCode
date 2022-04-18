'''
main idea: dfs
time comp: O(logn)
space comp: O(d)
- where n is the number of nodes in the BST and d is the depth of the BST

Note: I'm no idea whey failed to delete root node in test case 7. Maybe this is a bug.
'''

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		def dfs(node):
			if not node:
				return BST(value)
			if node.value > value:
				node.left = dfs(node.left)
			else:
				node.right = dfs(node.right)
			return node
		
        return dfs(self)

    def contains(self, value):
        # Write your code here.
        node = self
		while node:
			if node.value > value:
				node = node.left
			elif node.value == value:
				return True
			else:
				node = node.right
				
		return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		def dfs(node, value):
			if not node:
				return None
			
			if node.value > value:
				node.left = dfs(node.left, value)
			elif node.value < value:
				node.right = dfs(node.right, value)
			else:
				if not node.left:
					return node.right
				elif not node.right:
					return node.left
				else:
					p = node.right
					while p.left:
						p = p.left
					
					node.value = p.value
					node.right = dfs(node.right, p.value)
			return node
		
		return dfs(self, value)