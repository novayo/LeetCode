'''
main idea: color
time comp: O(v + e)
space comp: O(v)
- where v is the number of vertices and e is the number of edges in the graph
'''

WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph(edges):
    # Write your code here.
	def hasCycle(node):
		colored[node] = GREY
		
		for nei in edges[node]:
			if colored[nei] == GREY:
				return True
			if colored[nei] == BLACK:
				continue
			if hasCycle(nei):
				return True
		colored[node] = BLACK
		return False
	
	n = len(edges)
	colored = [WHITE] * n
	
	for node in range(n):
		if colored[node] != WHITE:
			continue
		
		if hasCycle(node):
			return True
	
    return False

