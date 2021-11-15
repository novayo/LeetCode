Question: https://leetcode.com/problems/coin-change/

---

try_1.java: O(n^2)
* Runtime: 9 ms, faster than 98.26% of Java online submissions for Coin Change.
* Memory Usage: 38.3 MB, less than 72.64% of Java online submissions for Coin Change.

> dp

---

try_2.py: O(n^2)

* Runtime: 1898 ms, faster than 32.81% of Python3 online submissions for Coin Change.
* Memory Usage: 14.5 MB, less than 64.11% of Python3 online submissions for Coin Change.

> dp => 由1開始去兌換，[1,2,5]可兌換的話，則dp[k] = min(dp[k-1], dp[k-2], dp[k-5])+1 => 從此點往前，看哪個兌換到k會是最小的

---

try_3.py: O(n*sum) O(sum)

* Runtime: 1468 ms, faster than 57.42% of Python3 online submissions for Coin Change.
* Memory Usage: 14.5 MB, less than 64.22% of Python3 online submissions for Coin Change.

> knapsack
