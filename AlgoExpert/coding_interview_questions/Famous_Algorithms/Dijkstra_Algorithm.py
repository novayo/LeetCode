'''
main idea: dijkstra
time comp: O(nlogn)
space comp: O(n)
- where n is the length of the input array
'''
import heapq

def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    hq = [(0, start)]
	
	ans = [-1] * len(edges)
	while hq:
		score, i = heapq.heappop(hq)
		
		if ans[i] != -1 and score >= ans[i]:
			continue
		
		ans[i] = score
		
		for des, dis in edges[i]:
			if ans[des] == -1 or score + dis < ans[des]:
				heapq.heappush(hq, (score + dis, des))
	return ans
		
