'''
main idea: sort
time comp: O(nlogn)
space comp: O(1)
- where n is the length of the input array
'''
def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	pre = ans = 0
	for query in queries:
		ans += pre
		pre += query
    return ans

