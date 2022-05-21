'''
main idea: greedy
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
'''
def sunsetViews(buildings, direction):
    # Write your code here.
    cur_max = 0
	ret = []
	
	if direction == 'EAST':
		for i in range(len(buildings)-1, -1, -1):
			if buildings[i] > cur_max:
				ret.append(i)
				cur_max = buildings[i]
		ret.reverse()
	else:
		for i in range(len(buildings)):
			if buildings[i] > cur_max:
				ret.append(i)
				cur_max = buildings[i]
	return ret
