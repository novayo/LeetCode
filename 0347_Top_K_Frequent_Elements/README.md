Question: https://leetcode.com/problems/top-k-frequent-elements/

---

try_1.py: O(nlogn)
* Runtime: 108 ms, faster than 61.19% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.5 MB, less than 9.05% of Python3 online submissions for Top K Frequent Elements.

> 用dictionary去儲存每個值出現的次數，排序value之後抓出對應的key即可。
> sort用的是timsort，因此時間複雜度為nlogn

---

try_2.py: O(nlogn)
* Runtime: 92 ms, faster than 92.79% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.9 MB, less than 16.31% of Python3 online submissions for Top K Frequent Elements.

> hash table + sort

---

try_3.py: O(klogk) O(k)

* Runtime: 92 ms, faster than 97.50% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.6 MB, less than 95.46% of Python3 online submissions for Top K Frequent Elements.

> 只紀錄長度為k的heap

---

try_4.py: O(n) O(n)

* Runtime: 88 ms, faster than 99.32% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.8 MB, less than 37.77% of Python3 online submissions for Top K Frequent Elements.

> quick select

---

try_5.py: O(n) O(n)

* Runtime: 108 ms, faster than 44.69% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 20.1 MB, less than 6.27% of Python3 online submissions for Top K Frequent Elements.

> bucket sort

---

try_6.py: O(n) O(n)

* Runtime: 174 ms, faster than 15.30% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.5 MB, less than 95.49% of Python3 online submissions for Top K Frequent Elements.

> quick select

---

try_7.py: O(n) O(n)

* Runtime: 112 ms, faster than 43.23% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 20.1 MB, less than 7.05% of Python3 online submissions for Top K Frequent Elements.

> bucket sort

---

try_8.py: O(nlogk) O(k)

* Runtime: 168 ms, faster than 17.86% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.8 MB, less than 39.49% of Python3 online submissions for Top K Frequent Elements.

> heap
