'''
main idea: counter
time comp: O(n*26)
space comp: O(26)
- where n is the length of the input bigString
'''

import collections

def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    counter1 = collections.Counter(bigString)
	counter2 = collections.Counter(smallString)
	
	ans = ''
	idx = 0
	while idx < len(bigString):
		counter = collections.Counter()
		for i in range(idx, len(bigString)):
			counter[bigString[i]] += 1
			if all(counter[k] >= counter2[k] for k in counter2.keys()):
				break
		
		if not all(counter[k] >= counter2[k] for k in counter2.keys()):
			break
		
		j = i
		while all(counter[k] >= counter2[k] for k in counter2.keys()):
			counter[bigString[idx]] -= 1
			idx += 1

		if not ans or len(ans) > len(bigString[idx-1: j+1]):
			print(bigString[idx-1: j+1])
			ans = bigString[idx-1: j+1]
	return ans
