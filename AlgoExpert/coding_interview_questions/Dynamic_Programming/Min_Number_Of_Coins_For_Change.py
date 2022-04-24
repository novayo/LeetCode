'''
main idea: recursion + memo
time comp: O(nd)
space comp: O(n)
- where n is the target amount and d is the length of the denoms
'''
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	memo = {}
	def recr(amount, idx):
		nonlocal ans
		
		if amount == 0:
			return 0
		
		if idx >= len(denoms) or amount < 0:
			return float('inf')
		
		if (amount, idx) not in memo:
			ret = recr(amount, idx+1)
			for i in range(1, amount // denoms[idx] + 1):
				ret = min(ret, i + recr(amount - i*denoms[idx], idx+1))
			memo[amount, idx] = ret
		return memo[amount, idx]
	
	ans = recr(n, 0) 
	return ans if ans < float('inf') else -1
