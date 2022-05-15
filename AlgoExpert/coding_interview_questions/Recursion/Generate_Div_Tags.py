'''
main idea: top down
time comp: O((2n)! / ((n!((n+1)!))))
space comp: O((2n)! / ((n!((n+1)!))))
- where n is the input integer
'''

def generateDivTags(numberOfTags):
    # Write your code here.
	LEFT, RIGHT = "<div>", "</div>"
	
	ans = []
	def dfs(l, r, cur):
		if l == numberOfTags and r == numberOfTags:
			ans.append(cur)
			return
		if l > numberOfTags or l < r:
			return
		
		dfs(l+1, r, cur+LEFT)
		dfs(l, r+1, cur+RIGHT)
	
	dfs(0, 0, "")
    return ans
