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

---

try_4.py: O(n*sum) O(n*sum)

* Runtime: 2144 ms, faster than 19.70% of Python3 online submissions for Coin Change.
* Memory Usage: 16.4 MB, less than 23.36% of Python3 online submissions for Coin Change.

> knapsack

---

try_5.py: O(m*n) O(m*n)

* Runtime: 2700 ms, faster than 7.96% of Python3 online submissions for Coin Change.
* Memory Usage: 16.2 MB, less than 24.51% of Python3 online submissions for Coin Change.

> knapsack

---

try_6.py: O(m*n) O(m*n)

* Runtime: 3762 ms, faster than 5.01% of Python3 online submissions for Coin Change.
* Memory Usage: 16 MB, less than 26.91% of Python3 online submissions for Coin Change.

> knapsack

---

try_7.py: O(m*n) O(m*n)

* Runtime: 915 ms, faster than 77.79% of Python3 online submissions for Coin Change.
* Memory Usage: 38.9 MB, less than 12.84% of Python3 online submissions for Coin Change.

> recursion

---

try_8.py: O(m*n) O(m)

* Runtime: 938 ms, faster than 74.03% of Python3 online submissions for Coin Change.
* Memory Usage: 16.7 MB, less than 63.81% of Python3 online submissions for Coin Change.

> dp
