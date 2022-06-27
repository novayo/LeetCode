Question: https://leetcode.com/problems/find-median-from-data-stream/

---

try_1.py:

* Runtime: 284 ms, faster than 26.29% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 24.3 MB, less than 6.67% of Python3 online submissions for Find Median from Data Stream.

> insertion sort

---

try_2.py: O(logn) O(1)

* Runtime: 192 ms, faster than 73.45% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 25.8 MB, less than 12.84% of Python3 online submissions for Find Median from Data Stream.

> 比中間大: min-heap、比中間小: max-heap
> 這樣抓取中間值只要取得 min-heap的第一位 & max-heap的第一位即可

---

try_3.py: O(n) O(n)

* Runtime: 3001 ms, faster than 7.62% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 35.3 MB, less than 97.86% of Python3 online submissions for Find Median from Data Stream.

> binary search(logn) + insert in list(n) => O(n)

---

try_4.py: O(logn) O(n)

* Runtime: 932 ms, faster than 28.57% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 35.9 MB, less than 70.92% of Python3 online submissions for Find Median from Data Stream.

> addNum => O(logn)、findMedian => O(1)
> 將arr分成兩半部，一個由小到大，一個由大到小 => 這樣就可以取得中間
> 如何維持 => 小的那半部長度 會比 大的那半部+1或相等，所以，要分情況去push

---

try_5.py: O(logn) O(n)

* Runtime: 621 ms, faster than 79.47% of Python3 online submissions for Find Median from Data Stream.
* Memory Usage: 36.5 MB, less than 13.80% of Python3 online submissions for Find Median from Data Stream.

> heap
