Question: https://leetcode.com/problems/maximum-subarray/
---

try_1.py: O(nlgn)

* Runtime: 156 ms, faster than 5.08% of Python3 online submissions for Maximum Subarray.
* Memory Usage: 13.7 MB, less than 37.40% of Python3 online submissions for Maximum Subarray.

> divide and conquer
	* divide: array into subarray
	* conquer: to sum up from left to middle to right
* Main Idea: 
	* conquer from break-down array to the original one
	* compare the value among left_array, left_middle_right, right_array in break-down array every single time

---

try_2.py: O(n)

* Runtime: 60 ms, faster than 98.58% of Python3 online submissions for Maximum Subarray.
* Memory Usage: 13.6 MB, less than 59.35% of Python3 online submissions for Maximum Subarray.

> straightforward
