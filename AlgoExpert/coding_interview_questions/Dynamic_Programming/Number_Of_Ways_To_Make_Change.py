'''
main idea: recrsion + memo
time comp: O(nd)
space comp: O(n)
- where n is the target amount and d is the number of coin denoms
'''
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	length = len(denoms)
	
	memo = {}
    def recr(amount, idx):
		if amount == 0:
			return 1
		
		if idx >= length or amount < 0:
			return 0
		
		if (amount, idx) not in memo:
			memo[amount, idx] = recr(amount-denoms[idx], idx) + recr(amount, idx+1)
		return memo[amount, idx]
	
	return recr(n, 0)

