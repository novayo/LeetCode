'''
main idea: dp
time comp: O(n)
space comp: O(1)
'''
def getNthFib(n):
    # Write your code here.
    if n == 1:
		return 0
	
	a, b = 0, 1
	for _ in range(n-2):
		c = a + b
		a = b
		b = c
		
	return b
