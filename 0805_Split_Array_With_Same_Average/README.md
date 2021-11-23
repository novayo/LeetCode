Question: https://leetcode.com/problems/split-array-with-same-average/

---

try_1.py: O(N*N*sum) O(N*N*sum)

* TLE

> dp[i][k][n] = 前i個，取k個，能否組成n = False => 這個代表sumA

---

try_2.py: O(n^2) O(n^2)

* Runtime: 748 ms, faster than 25.19% of Python3 online submissions for Split Array With Same Average.
* Memory Usage: 79.1 MB, less than 19.17% of Python3 online submissions for Split Array With Same Average.

> 因為knapsack的定義是sum(nums)，當總和很大，不管長度小或大，都會TLE
> 那就乾脆找出取前k個的組合
> 最後一樣檢查取k個時的合理A是否能被組成
