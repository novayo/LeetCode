Question: https://leetcode.com/problems/maximum-performance-of-a-team/

---

try_1.py: O(nlogn)
* Runtime: 412 ms, faster than 91.72% of Python3 online submissions for Maximum Performance of a Team.
* Memory Usage: 28.8 MB, less than 100.00% of Python3 online submissions for Maximum Performance of a Team.

> Priority Queue
	> 在每次測試的時候，去保證現在的sum是最大的
	> 而sum由兩個因素來決定，
	> 先看右邊的元素，取min，所以若要讓這個值最大，則把efficiency由高到低去拿
	> 在看左邊的元素，是相加的，所以從現在的sum中剔除一個時（能測試下一個組合），把左邊的最小值給剃除掉（相對的右邊也要跟著剔除）
