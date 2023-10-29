costs = [80, 40, 30, 40, 20]
values = [20, 50, 50, 30, 20]
numbers = [4, 9, 7, 6, 1]

maxCost = 1000


dp = [0] * (maxCost+1) # dp[1000]的最大價值

for i in range(len(values)):
    for _maxCost in range(maxCost, -1, -1):
        for num in range(numbers[i]+1):
            if _maxCost-(costs[i] * num) < 0:
                continue
            dp[_maxCost] = max(dp[_maxCost], dp[_maxCost-(costs[i] * num)] + values[i] * num)
print(dp[maxCost])