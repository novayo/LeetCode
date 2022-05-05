'''
main idea: sort
time comp: O(n^2 + nlogn)
space comp: O(n)
- where n is the length of the input array
'''
def rectangleMania(coords):
    # Write your code here.
	coords.sort()
	
	coords_set = set()
	for coord in coords:
		coords_set.add(tuple(coord))
	
	ans = 0
	for i, (x, y) in enumerate(coords):
		for j in range(i+1, len(coords)):
			x1, y1 = coords[j]
			
			if x == x1 or y >= y1:
				continue
			
			if (x, y1) in coords_set and (x1, y) in coords_set:
				ans += 1
	return ans
