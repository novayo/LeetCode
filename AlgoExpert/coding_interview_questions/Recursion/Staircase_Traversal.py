'''
main idea: dfs
time comp: O(maxSteps ** height)
space comp: O(height)
- where maxSteps and height are the input integer
'''

def staircaseTraversal(height, maxSteps):
    # Write your code here.
	
	def dfs(h):
		if h > height:
			return 0
		if h == height:
			return 1
		
		ret = 0
		for step in range(1, maxSteps+1):
			ret += dfs(h+step)
		return ret
	
    return dfs(0)
