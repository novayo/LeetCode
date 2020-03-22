Question: https://leetcode.com/problems/largest-rectangle-in-histogram/

---

try_1.py: O(nlogn)
* Runtime: 668 ms, faster than 5.29% of Python3 online submissions for Largest Rectangle in Histogram.
* Memory Usage: 63.8 MB, less than 9.09% of Python3 online submissions for Largest Rectangle in Histogram.

> O(n) for finding left and right part
> O(logn) for finding min index at that range
	> using segment tree to implement it 
