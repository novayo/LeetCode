'''
main idea: deque
time comp: O(n)
space comp: O(n)
- where n is the length of the input string
'''

import collections

def longestSubstringWithoutDuplication(string):
    # Write your code here.
    deq = collections.deque()
	found = set()
	
	ans = ''
	for s in string:
		if s not in found:
			deq.append(s)
			found.add(s)
			
			if len(deq) > len(ans):
				ans = ''.join(deq)
		else:
			while deq[0] != s:
				found.remove(deq.popleft())
			deq.popleft()
			deq.append(s)
	return ans
