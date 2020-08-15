Question: https://leetcode.com/problems/search-insert-position/

---

try_1.py: O(logn)
* Runtime: 40 ms, faster than 98.99% of Python3 online submissions for Search Insert Position.
* Memory Usage: 14.7 MB, less than 5.38% of Python3 online submissions for Search Insert Position.

> 用binary search去搜尋
> 一個值得注意的點是，因為可能會插入在整個陣列的尾端，因此資料範圍不是從0~len-1，而是0~len，因為right應要包含到所有可能的資料範圍之中
