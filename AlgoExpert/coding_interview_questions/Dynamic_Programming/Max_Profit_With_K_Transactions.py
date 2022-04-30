'''
main idea: state dp
time comp: O(nk)
space comp: O(nk)
- where n is the length of the input array and k is the integer parameter
'''
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    n = len(prices)
	dp = [[-float('inf'), -float('inf')] for _ in range(k+1)]
	
	dp[-1][0] = 0
	for price in prices:
		for i in range(k+1):
			if i < k:
				dp[i][0] = max(dp[i][0], dp[i+1][1] + price)
			dp[i][1] = max(dp[i][1], dp[i][0] - price)
	
	return max([d[0] for d in dp])
