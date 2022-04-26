'''
main idea: knap dp
time comp: O(nc)
space comp: O(nc)
- where n is the length of items and c is the capacity
'''
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
	n = len(items)
	
    def recr(idx, capacity):
		if idx >= n:
			return [0, []]
		
		not_choose = recr(idx+1, capacity)
		if capacity - items[idx][1] >= 0:
			choose = recr(idx+1, capacity - items[idx][1])
			choose[0] += items[idx][0]
			choose[1].append(idx)

			if choose[0] >= not_choose[0]:
				return choose
			else:
				return not_choose
		else:
			return not_choose
				
	return recr(0, capacity)