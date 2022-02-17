Question: https://leetcode.com/problems/largest-divisible-subset/

---

try_1.py: O(n^2) O(n)

* Runtime: 296 ms, faster than 95.32% of Python3 online submissions for Largest Divisible Subset.
* Memory Usage: 14.3 MB, less than 94.88% of Python3 online submissions for Largest Divisible Subset.

> 排序好後，每個index 找 之前list中最大的數值 % == 0 => 代表跟此list其餘的也可以整除

---

try_2.py: O(n^2) O(n*len(ans))

* Runtime: 484 ms, faster than 16.50% of Python3 online submissions for Largest Divisible Subset.
* Memory Usage: 14.5 MB, less than 67.28% of Python3 online submissions for Largest Divisible Subset.

> dp[i] = 前i個，能組成的最長元素
> dp[i] = dp[0~i-1] 中的最長 & +上自己
> 留最大即可

---

try_3.py: O(n^2) O(n)

* Runtime: 824 ms, faster than 16.81% of Python3 online submissions for Largest Divisible Subset.
* Memory Usage: 14.3 MB, less than 68.53% of Python3 online submissions for Largest Divisible Subset.

> LIS (要記得先sort)

---

try_4.py: O(n^2) O(n)

* Runtime: 1001 ms, faster than 8.87% of Python3 online submissions for Largest Divisible Subset.
* Memory Usage: 14.1 MB, less than 94.86% of Python3 online submissions for Largest Divisible Subset.

> LIS + sort => without copy