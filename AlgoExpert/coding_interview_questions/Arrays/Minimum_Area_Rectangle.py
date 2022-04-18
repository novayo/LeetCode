'''
main idea: sort
time comp: O(n^2)
space comp: O(n)
- where n is the length of points
'''
def minimumAreaRectangle(points):
    # Write your code here.
	def same(p1, p2):
		return p1[0] == p2[0] or p1[1] == p2[1] or p1[1] > p2[1]
		
    ans = float('inf')
	n = len(points)
	
	s_points = set([tuple(p) for p in points])
	
	points.sort()
	for i in range(n):
		for j in range(i+1, n):
			if same(points[i], points[j]):
				continue
			
			_ans = abs(points[j][0] - points[i][0]) * abs(points[j][1] - points[i][1])
			if _ans >= ans:
				break
				
			p1 = (points[i][0], points[j][1])
			p2 = (points[j][0], points[i][1])
			
			if (p1 in s_points and p2 in s_points):
				ans = min(ans, _ans)
				break
	
	return ans if ans < float('inf') else 0
