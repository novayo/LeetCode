'''
main idea: sort
time comp: O(nlogn)
space comp: O(n)
- where n is the length of the input array
'''
def taskAssignment(k, tasks):
    # Write your code here.
	tasks = [(task, i) for i, task in enumerate(tasks)]
	tasks.sort()
	
	ans = []
	for i in range(k):
		ans.append([tasks[i][1], tasks[~i][1]])
    return ans

