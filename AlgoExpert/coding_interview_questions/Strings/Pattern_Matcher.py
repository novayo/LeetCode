'''
main idea: backtracking
time comp: O(n^m)
space comp: O(n^m)
- where n is the length of the string and m is the length of the pattern
'''
def patternMatcher(pattern, string):
    # Write your code here.
    n = len(pattern)
	m = len(string)
	
	matchTable = {}
	found = set()
	def recr(idx_p, idx_s):
		print(matchTable)
		if idx_p >= n and idx_s >= m:
			return True
		elif idx_p >= n or idx_s >= m:
			return False
		
		if pattern[idx_p] in matchTable:
			pat = matchTable[pattern[idx_p]]
			if string[idx_s: idx_s+len(pat)] == pat:
				if recr(idx_p+1, idx_s+len(pat)):
					return True
			return False
		
		for i in range(idx_s, m):
			pat = string[idx_s: i+1]
			if pat in found:
				continue
			
			found.add(pat)
			matchTable[pattern[idx_p]] = pat
			if recr(idx_p+1, i+1):
				return True
			found.remove(pat)
			del matchTable[pattern[idx_p]]
		
		return False
	if recr(0, 0):
		return matchTable.get('x', ''), matchTable.get('y', '')
	return []
