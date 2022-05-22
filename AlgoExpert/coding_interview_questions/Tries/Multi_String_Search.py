'''
main idea: trie
time comp: O(n^2 + m)
space comp: O(n^2)
- where n is the length of the bigString and m is the length of the smallStrings
'''
def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    root = {}
	for i in range(len(bigString)):
		r = root
		for s in bigString[i:]:
			if s not in r:
				r[s] = {}
			r = r[s]
		r['*'] = True
	
	ans = []
	for string in smallStrings:
		r = root
		flag = True
		for s in string:
			if s not in r:
				flag = False
				break
			r = r[s]
		
		ans.append(flag)
	
	return ans
