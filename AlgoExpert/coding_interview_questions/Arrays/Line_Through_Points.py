'''
main idea: y=mx+b
time comp: O(n^2)
space comp: O(n)
- where n is the number of points
'''
import collections

def lineThroughPoints(points):
    # Write your code here.
	def function(p1, p2):
		if p1[0] == p2[0]:
			return ('x', p1[0])
		elif p1[1] == p2[1]:
			return ('y', p1[1])
		
		# y = mx+b => b = y-mx
		slope = (p2[1]-p1[1]) / (p2[0]-p1[0])
		b = p1[1] - slope * p1[0]
		return (slope, b)
	
	n = len(points)
	points.sort()
	counter = collections.defaultdict(set)
	for i in range(n):
		for j in range(i+1, n):
			counter[function(points[i], points[j])].add(i)
			counter[function(points[i], points[j])].add(j)
	
	ans = 1
	for k, v in counter.items():
		ans = max(ans, len(v))
	return ans
