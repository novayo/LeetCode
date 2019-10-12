Question: https://leetcode.com/problems/maximum-subarray/
---

try_1.py: O(nlgn) 144ms
> divide and conquer
	* divide: array into subarray
	* conquer: to sum up from left to middle to right
* Main Idea: 
	* conquer from break-down array to the original one
	* compare the value among left_array, left_middle_right, right_array in break-down array every single time
