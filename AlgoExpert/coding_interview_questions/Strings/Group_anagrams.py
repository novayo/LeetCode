'''
main idea: sort
time comp: O(n*(mlogm))
space comp: O(n*m)
- where n is the length of the input words and m is the max length of the word in words
'''
def groupAnagrams(words):
    # Write your code here.
    indicies = {}
	ans = []
	
	for w in words:
		t = ''.join(sorted(w))
		if t not in indicies:
			indicies[t] = len(ans)
			ans.append([w])
		else:
			ans[indicies[t]].append(w)
	return ans

