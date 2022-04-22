'''
main idea: dfs bottom up
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in the input tree and d is the depth of the input tree
'''

def allKindsOfNodeDepths(root):
    # Write your code here.
	ans = 0
    def dfs(node):
		nonlocal ans
		
		if not node:
			return 0, 0
		
		num = ret = 0
		if node.left:
			left = dfs(node.left)
			ret += left[0]
			num += left[1]
		if node.right:
			right = dfs(node.right)
			ret += right[0]
			num += right[1]
		
		ans += ret + num
		return ret + num, num + 1
	dfs(root)
	return ans


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
