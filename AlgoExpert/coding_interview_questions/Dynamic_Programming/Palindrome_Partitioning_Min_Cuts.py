'''
main idea: find all palindrome + dijastra
time comp: O(n^2)
space comp: O(n^2)
- where n is the length of the input string
'''

import collections
import heapq

def palindromePartitioningMinCuts(string):
    # Write your code here.
	d = findAllPalindrome(string)
	hq = [(0, 0)]
	cache = set([0])
	
	while hq:
		step, pos = heapq.heappop(hq)
		pos *= -1
		
		if pos == len(string):
			return step-1
		
		for _next in d[pos]:
			if _next+1 in cache:
				continue
			cache.add(_next+1)
			heapq.heappush(hq, (step+1, -(_next+1)))

def findAllPalindrome(string):
	def expand(idx1, idx2):
		l, r = idx1-1, idx2+1
		while l >= 0 and r < len(string) and string[l] == string[r]:
			l -= 1
			r += 1
		return l+1, r-1
	
	d = collections.defaultdict(list)
	for i in range(len(string)):
		l, r = expand(i, i)
		d[l].append(r)
		
		if i > 0 and string[i-1] == string[i]:
			l, r = expand(i-1, i)
			d[l].append(r)
	return d
