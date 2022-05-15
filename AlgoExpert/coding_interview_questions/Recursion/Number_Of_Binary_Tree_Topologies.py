'''
main idea: dfs + memo
time comp: O((n*(2n)!) / (n!(n+1)!))
space comp: O(n)
- where n is the input integer
'''
def numberOfBinaryTreeTopologies(n):
    # Write your code here.
	
	memo = {}
	def dfs(n):
		if n <= 1:
			return 1
		
		if n not in memo:
			ret = 0
			left = n
			for right in range(n):
				left -= 1

				ret += dfs(left) * dfs(right)
			memo[n] = ret
		return memo[n]
	
    return dfs(n)
