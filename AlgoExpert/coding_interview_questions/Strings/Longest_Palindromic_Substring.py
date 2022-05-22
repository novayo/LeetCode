'''
main idea: expand from center
time comp: O(n^2)
space comp: O(n)
- where n is the length of the input string
'''
def longestPalindromicSubstring(string):
    # Write your code here.
	ans = ''
    for i in range(len(string)):
		ret = expand_from_center(i, i, string)
		if len(ret) > len(ans):
			ans = ret
		if i > 0 and string[i-1] == string[i]:
			ret = expand_from_center(i-1, i, string)
			if len(ret) > len(ans):
				ans = ret
	return ans

def expand_from_center(i, j, string):
	while i-1 >= 0 and j+1 < len(string) and string[i-1] == string[j+1]:
		i -= 1
		j += 1
	return string[i:j+1]
