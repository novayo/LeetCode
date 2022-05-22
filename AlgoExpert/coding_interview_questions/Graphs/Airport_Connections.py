'''
main idea: bfs
time comp: O(n)
space comp: O(n)
- where n is the length of the airports
'''

import collections

class Node:
	def __init__(self):
		self.children = []
		self.parents = []
		self.layer = 0

def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    graph = collections.defaultdict(Node)
	for a, b in routes:
		graph[a].children.append(b)
		graph[b].parents.append(a)
	
	# mark layer from startingAirport
	queue = [startingAirport]
	cache = set([startingAirport])
	layer = 0
	while queue:
		next_queue = []
		for node in queue:
			graph[node].layer = layer
			for parent in graph[node].parents:
				if parent in cache:
					continue
				cache.add(parent)
				next_queue.append(parent)
		layer -= 1
		queue = next_queue
	
	# start from startingAirport child
	ignores = set()
	bfs(startingAirport, graph, ignores)
	
	# start from parent 0 ~ n and layer lower ~ 0
	order = []
	for a in airports:
		order.append((len(graph[a].parents), graph[a].layer, a))
	order.sort()
	
	ans = 0
	for _, _, a in order:
		if a not in ignores:
			ans += 1
			bfs(a, graph, ignores)
	
	return ans
	
def bfs(start, graph, ignores):
	ignores.add(start)
	queue = collections.deque([start])
	while queue:
		node = queue.popleft()
		
		for child in graph[node].children:
			if child not in ignores:
				ignores.add(child)
				queue.append(child)
