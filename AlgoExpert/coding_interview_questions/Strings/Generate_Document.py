'''
main idea: count
time comp: O(n)
space comp: O(n)
- where n is the max length of the input string
'''

import collections

def generateDocument(characters, document):
    # Write your code here.
	counter = collections.Counter(characters)
	
	for s in document:
		if counter[s] > 0:
			counter[s] -= 1
		else:
			return False
	
    return True

