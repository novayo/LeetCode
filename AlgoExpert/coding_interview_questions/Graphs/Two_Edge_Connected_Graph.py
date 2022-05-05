'''
main idea: check the depth is equals to depth of dfs
time comp: O(v+e)
space comp: O(v)
- where v is the number of vertices of the input graph and e is the number of edges of the input graph
'''
def twoEdgeConnectedGraph(edges):
    # Write your code here.
	if not edges:
		return True
	
	n = len(edges)
	visited = [-1] * n
	
	def dfs(node, parent, depth):
		visited[node] = depth
		
		for e in edges[node]:
			if visited[e] == -1:
				visited[node] = min(visited[node], dfs(e, node, depth+1))
			elif e != parent:
				visited[node] = min(visited[node], visited[e])
		
		if visited[node] == depth and parent != -1:
			return -1
		
		return visited[node]
	
    dfs(0, -1, 0)
	return all([v != -1 for v in visited])

