'''
main idea: dp[i:]
time comp: O(mn)
space comp: O(mn)
- where m and n is the length of the two input strings
'''
def longestCommonSubsequence(str1, str2):
    # Write your code here.
	n1 = len(str1)
	n2 = len(str2)
	
	memo = {}
    def recr(idx1, idx2):
		if idx1 >= n1 or idx2 >= n2:
			return []
		
		if (idx1, idx2) not in memo:
			if str1[idx1] == str2[idx2]:
				memo[idx1, idx2] = [str1[idx1]] + recr(idx1+1, idx2+1)
			else:
				l = recr(idx1+1, idx2)
				r = recr(idx1, idx2+1)

				if len(l) >= len(r):
					memo[idx1, idx2] = l
				else:
					memo[idx1, idx2] = r
				
		return memo[idx1, idx2]
	
	return recr(0, 0)
