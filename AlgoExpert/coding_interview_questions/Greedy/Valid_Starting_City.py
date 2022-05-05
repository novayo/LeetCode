'''
main idea: dp
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
'''
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
	n = len(distances)
	dp = []
	for d, f in zip(distances, fuel):
		dp.append(f*mpg-d)
	
	ans = cur_sum = 0
	for i, d in enumerate(dp):
		if cur_sum < 0:
			cur_sum = 0
			ans = i
		cur_sum += d
	
    return ans

