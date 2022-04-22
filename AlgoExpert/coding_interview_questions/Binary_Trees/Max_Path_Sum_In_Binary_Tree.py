'''
main idea: dfs
time comp: O(n)
space comp: O(d)
- where n is the number of nodes in input tree and d is the depth of the input tree
'''
def maxPathSum(tree):
    # Write your code here.
	ans = -float('inf')
	
    def dfs(node):
		nonlocal ans
		
		if not node:
			return 0
		
		left = dfs(node.left)
		right = dfs(node.right)
	
		ret = node.value
		ret = max(ret, ret + left)
		ret = max(ret, ret + right)
		ans = max(ans, ret)
		return node.value + max(left, right)
	
	dfs(tree)
	return ans

