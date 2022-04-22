'''
main idea: dfs bottom-up
time comp: O(n)
space comp: O(n)
- where n is the number of nodes in input tree
'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    def dfs(node):
		if not node:
			return []
		
		if not node.left and not node.right:
			return [node.value]
		
		ret = []
		left = dfs(node.left)
		right = dfs(node.right)
		
		for l in left:
			ret.append(node.value + l)
		for r in right:
			ret.append(node.value + r)
		
		return ret
	
	return dfs(root)
		

