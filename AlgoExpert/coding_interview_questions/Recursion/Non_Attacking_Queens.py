'''
main idea: top down
time comp: O(n!)
space comp: O(n)
- where n is the input integer
'''

def nonAttackingQueens(n):
    # Write your code here.
	ans = 0
	
	cols = set()
	diag = set()
	anti_diag = set()
	
	def dfs(i):
		nonlocal ans
		
		if i >= n:
			ans += 1
			return
		
		for j in range(n):
			if j in cols or i-j in diag or i+j in anti_diag:
				continue
			cols.add(j)
			diag.add(i-j)
			anti_diag.add(i+j)
			
			dfs(i+1)
			
			cols.remove(j)
			diag.remove(i-j)
			anti_diag.remove(i+j)
	
	dfs(0)
    return ans
