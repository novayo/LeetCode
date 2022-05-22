'''
main idea: count
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''

import collections

def minimumCharactersForWords(words):
    # Write your code here.
	table = collections.defaultdict(int)
	for word in words:
		counter = collections.Counter(word)
		
		for k, v in counter.items():
			if v > table[k]:
				table[k] = v
		
	ret = []
    for k, v in table.items():
		for _ in range(v):
			ret.append(k)
	return ret

