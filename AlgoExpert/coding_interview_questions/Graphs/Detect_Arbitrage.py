'''
main idea: dfs
time comp: O(n^3)
space comp: O(n^2)
- where n is the number of currencies
'''
def detectArbitrage(exchangeRates):
    # Write your code here.
	
	def dfs(current, i, cache):
		if i == 0 and current > 1:
			return True
		
		for j, v in enumerate(exchangeRates[i]):
			if i == j or j in cache:
				continue
			
			cache.add(j)
			if dfs(current * v, j, cache):
				return True
			cache.remove(j)
		return False
	
    return dfs(1, 0, set())

