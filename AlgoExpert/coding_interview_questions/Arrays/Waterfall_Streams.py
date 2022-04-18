'''
main idea: bfs
time comp: O(w^2 * h)
space comp: O(w)
- where w and h is the width and height of the input array
'''
import collections

def waterfallStreams(array, source):
    # Write your code here.
	LEFT, RIGHT, DOWN= 0, 1, 2
	height = len(array)
	width = len(array[0])
	
    queue = collections.deque()
	queue.appendleft((0, source, DOWN, 1)) # i, j, face, percent
	
	ans = [0] * width

	while queue:
		i, j, face, percent = queue.pop()
		
		if (i == height-1):
			ans[j] += percent
			continue
		
		if (array[i+1][j] == 0):
			queue.appendleft((i+1, j, DOWN, percent))
			continue
			
		if (face == DOWN):
			if (j > 0 and array[i][j-1] == 0):
				queue.appendleft((i, j-1, LEFT, percent/2))
			if (j < width-1 and array[i][j+1] == 0):
				queue.appendleft((i, j+1, RIGHT, percent/2))
		elif (face == LEFT):
			if (j > 0 and array[i][j-1] == 0):
				queue.appendleft((i, j-1, LEFT, percent))
		elif (face == RIGHT):
			if (j < width-1  and array[i][j+1] == 0):
				queue.appendleft((i, j+1, RIGHT, percent))
	
	return [a * 100 for a in ans]
		