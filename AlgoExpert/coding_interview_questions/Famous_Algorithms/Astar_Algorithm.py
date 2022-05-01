'''
main idea: A*
time comp: O(nlogn)
space comp: O(n)
- where n is the number of element in graph
'''

import heapq

def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    # Write your code here.
    def estimate(i, j):
		return abs(endRow-i) + abs(endCol-j)
	
	height = len(graph)
	width = len(graph[0])
	
	steps = {}
	cache = set([(startRow, startCol)])
	hq = [(0, estimate(startRow, startCol), startRow, startCol)]
	
	while hq:
		step, score, i, j = heapq.heappop(hq)
		steps[i, j] = step
		
		if i == endRow and j == endCol:
			break
		
		for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
			if not (0 <= x < height and 0 <= y < width) or graph[x][y] == 1:
				continue
			
			if (x, y) in cache:
				continue
			
			cache.add((x, y))
			heapq.heappush(hq, (step+1, estimate(x, y), x, y))
	
	if (endRow, endCol) not in steps:
		return []
	
	i, j = endRow, endCol
	ans = [[i, j]]
	cur = steps[i, j]
	while cur != 0:
		for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
			if not (0 <= x < height and 0 <= y < width) or (x, y) not in steps:
				continue
			if steps[x, y] == cur-1:
				ans.append([x, y])
				cur -= 1
				i, j = x, y
	
	return ans[::-1]


