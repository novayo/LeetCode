'''
main idea: binary index tree
time comp: O(nlogn)
space comp: O(n)
- where n is the length of the input array
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

def rightSmallerThan(array):
    # Write your code here.
	indices = {}
    for i, v in enumerate(sorted(set(array))):
		indices[v] = i+1
	
	ans = [0] * len(array)
	tree = BIT(len(indices))
	for i in range(len(array)-1, -1, -1):
		idx = indices[array[i]]
		ans[i] = tree.query(idx-1)
		tree.update(idx)
	return ans