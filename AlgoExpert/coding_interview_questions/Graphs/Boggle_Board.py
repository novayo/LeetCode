'''
main idea: dfs
time comp: O(nm*8^s)
space comp: O(nm)
- where n is the width of the board, m is the height of the board and s is the length of the longest word
'''
import collections

def boggleBoard(board, words):
    # Write your code here.
	height = len(board)
	width = len(board[0])
	
    def dfs(string, i, j, cache):
		if string == "":
			return True
		
		for x, y in [i-1, j], [i-1, j+1], [i, j+1], [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1], [i-1, j-1]:
			if not (0 <= x < height and 0 <= y < width) or (x, y) in cache or board[x][y] != string[0]:
				continue
			cache.add((x, y))
			if dfs(string[1:], x, y, cache):
				return True
		return False
	
	table = collections.defaultdict(list)
	for word in words:
		table[word[0]].append(word)
	
	memo = set()
	ans = []
	for i in range(height):
		for j in range(width):
			for word in table[board[i][j]]:
				if word in memo:
					continue
				if dfs(word[1:], i, j, set([(i, j)])):
					ans.append(word)
					memo.add(word)
	return ans
