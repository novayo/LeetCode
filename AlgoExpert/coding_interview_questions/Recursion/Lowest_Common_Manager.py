'''
main idea: dfs
time comp: O(nodes)
space comp: O(H)
- where nodes is number of nodes in input tree and H is the hight of tree
'''

def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
	ans = None
	
	def dfs(node):
		nonlocal ans
		if ans:
			return 0
		
		if not node:
			return 0
		
		hit = 0
		if node == reportOne or node == reportTwo:
			hit += 1
		
		for child in node.directReports:
			hit += dfs(child)
		
		if hit == 2 and not ans:
			ans = node
		return hit
	
	dfs(topManager)
	return ans
	

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
