Question: https://leetcode.com/problems/find-median-from-data-stream/

---

try_1.py:

* Runtime: 284 ms, faster than 26.29% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 24.3 MB, less than 6.67% of Python3 online submissions for Find Median from Data Stream.

> insertion sort

try_2.py: O(logn) O(1)

* Runtime: 192 ms, faster than 73.45% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 25.8 MB, less than 12.84% of Python3 online submissions for Find Median from Data Stream.

> 比中間大: min-heap、比中間小: max-heap
> 這樣抓取中間值只要取得 min-heap的第一位 & max-heap的第一位即可