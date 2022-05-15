'''
main idea: dfs
time comp: O(2^k)
space comp: O(k)
- where k is the length of the three
'''

def interweavingStrings(one, two, three):
    # Write your code here.
    
	def dfs(i, j, k):
		if k >= len(three):
			return i >= len(one) and j >= len(two)
		
		if i < len(one) and one[i] == three[k]:
			if dfs(i+1, j, k+1):
				return True
		if j < len(two) and two[j] == three[k]:
			if dfs(i, j+1, k+1):
				return True
		
		return False
	
	return dfs(0, 0, 0)
