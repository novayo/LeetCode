'''
main idea: store prev status
time comp: O(1)
space comp: O(1)
'''
# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.min_max_stack = []
		self.stack = []
	
    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        ret = self.stack.pop()
		self.min_max_stack.pop()
		return ret

    def push(self, number):
        # Write your code here.
        pair = [number, number] # min, max
		if self.min_max_stack:
			pair[0] = min(pair[0], self.min_max_stack[-1][0])
			pair[1] = max(pair[1], self.min_max_stack[-1][1])
		self.min_max_stack.append(pair)
		self.stack.append(number)

    def getMin(self):
        # Write your code here.
        return self.min_max_stack[-1][0]

    def getMax(self):
        # Write your code here.
        return self.min_max_stack[-1][1]

