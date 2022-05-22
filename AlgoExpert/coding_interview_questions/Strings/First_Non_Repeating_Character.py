'''
main idea: counter
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''
import collections

def firstNonRepeatingCharacter(string):
    # Write your code here.
    counter = collections.Counter(string)
	
	for i, s in enumerate(string):
		if counter[s] == 1:
			return i
	
	return -1
