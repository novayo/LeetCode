'''
main idea: binary indexed tree
time comp: O(nlogn)
space comp: O(n)
'''
class BIT:
	def __init__(self, n):
		self.arr = [0] * (n+1)
	
	def update(self, idx, delta=1):
		while idx < len(self.arr):
			self.arr[idx] += delta
			idx += idx & -idx
	
	def query(self, idx):
		ret = 0
		while idx > 0:
			ret += self.arr[idx]
			idx -= idx & -idx
		return ret

def countInversions(array):
    # Write your code here.
	sort_array_set = sorted(list(set(array)))
	indicies = {}
	for i, v in enumerate(sort_array_set):
		indicies[v] = i

	ans = 0
	tree = BIT(len(sort_array_set))
	for v in array[::-1]:
		idx = indicies[v]
		ans += tree.query(idx)
		tree.update(idx+1)
	return ans
