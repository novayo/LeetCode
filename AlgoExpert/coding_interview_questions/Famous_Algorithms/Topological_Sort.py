'''
main idea: topological sort
time comp: (V+E)
space comp: (V+E)
- where V is the number of jobs and E is the number of dependencies
'''
import collections

class Node:
	def __init__(self):
		self.children = []
		self.parents = 0

def topologicalSort(jobs, deps):
    # Write your code here.
    graph = {}
	for job in jobs:
		graph[job] = Node()
	
	number_edges = 0
	for a, b in deps:
		graph[a].children.append(b)
		graph[b].parents += 1
		number_edges += 1
	
	queue = collections.deque()
	for job in jobs:
		if graph[job].parents == 0:
			queue.append(job)
	
	ans = []
	removed_edges = 0
	while queue:
		job = queue.popleft()
		ans.append(job)
		
		for c in graph[job].children:
			removed_edges += 1
			graph[c].parents -= 1
			if graph[c].parents == 0:
				queue.append(c)
	return ans if number_edges == removed_edges else []
		
